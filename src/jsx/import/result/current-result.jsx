/**
 * current-display.jsx: display current prediction result.
 *
 * @CurrentResultDisplay, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';
import { Table } from 'react-bootstrap';
import queryString from 'query-string';
import { setLayout, setContentType, setResultsButton } from '../redux/action/page.jsx';
import Submit from '../general/submit-button.jsx';
import Spinner from '../general/spinner.jsx';
import ajaxCaller from '../general/ajax-caller.js';

class CurrentResultDisplay extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state = {
            nid: null,
            computed_result: null,
            computed_type: null,
            display_spinner: false,
            ajax_done_result: false, 
            ajax_retrieval_result: {},
        };
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    // send form data to serverside on form submission
    handleSubmit(event) {
        // prevent page reload
        event.preventDefault();

        // local variables
        const ajaxEndpoint = '/save-prediction';

        // ajax process
        if (this.state.computed_result && this.state.computed_type) {
            var formData = new FormData(this.refs.savePredictionForm);
            formData.append('status', 'valid');
            formData.append('data', this.state.computed_result);
            formData.append('model_type', this.state.computed_type);

            var ajaxArguments = {
                endpoint: ajaxEndpoint,
                data: formData,
            };
        } else {
            var formData = new FormData(this.refs.savePredictionForm);
            formData.append('status', 'no-data');

            var ajaxArguments = {
                endpoint: ajaxEndpoint,
                data: formData,
            };
        }

        // boolean to show ajax spinner
        this.setState({ display_spinner: true });

        // asynchronous callback: ajax 'done' promise
        ajaxCaller(
            (asynchObject) => {
                // Append to DOM
                if (asynchObject && asynchObject.error) {
                    this.setState({ ajax_store_error: asynchObject.error });
                } else if (asynchObject) {
                    this.setState({ ajax_store_result: asynchObject });

                    const action = setResultsButton({ button: { review_results: true } });
                    this.props.dispatchResultsButton(action);
                } else {
                    this.setState({ ajax_store_result: null });
                }
                // boolean to hide ajax spinner
                this.setState({ display_spinner: false });
            },
            // asynchronous callback: ajax 'fail' promise
            (asynchStatus, asynchError) => {
                if (asynchStatus) {
                    this.setState({ ajax_store_status: asynchStatus });
                    console.log(`Error Status: ${asynchStatus}`);
                }
                if (asynchError) {
                    this.setState({ ajax_store_error: asynchError });
                    console.log(`Error Thrown: ${asynchError}`);
                }
                // boolean to hide ajax spinner
                this.setState({ display_spinner: false });
            },
            // pass ajax arguments
            ajaxArguments,
        );
    }
    // define properties after update
    componentDidUpdate() {
        if (
            this.props &&
            this.props.results &&
            !!this.props.results.data &&
            !!this.props.results.type &&
            this.state.computed_result != JSON.stringify(this.props.results.data)
        ) {
            this.setState({
                computed_result: JSON.stringify(this.props.results.data),
                computed_type: this.props.results.type,
            });
        }
    }
    componentWillMount() {
        if (
            !!this.props &&
            !!this.props.location
        ) {
            const parsed = queryString.parse(this.props.location.search);
            if (!!parsed && !!parsed.nid) {
                this.setState({ nid: parsed.nid });
            }
        }

        // update redux store: define overall page layout
        const action = setLayout({ layout: 'analysis' });
        this.props.dispatchLayout(action);

        const actionContentType = setContentType({ layout: 'result' });
        this.props.dispatchContentType(actionContentType);
    }
    componentDidMount() {
        // execute if 'nid' defined from 'componentWillMount'
        if (this.state && !!this.state.nid) {
            // ajax arguments
            const data = new FormData();
            data.append('id_result', this.state.nid);
            const ajaxEndpoint = '/retrieve-prediction';
            const ajaxArguments = {
                endpoint: ajaxEndpoint,
                data,
            };

            // boolean to show ajax spinner
            if (
                this.state &&
                !this.state.display_spinner &&
                !this.state.ajax_done_result
            ) {
                this.setState({ display_spinner: true });
            }

            // asynchronous callback: ajax 'done' promise
            ajaxCaller(
                (asynchObject) => {
                    // Append to DOM
                    if (asynchObject && asynchObject.error) {
                        this.setState({ ajax_retrieval_error: asynchObject.error });
                    } else if (asynchObject) {
                        this.setState({ ajax_retrieval_result: asynchObject });
                    } else {
                        this.setState({ ajax_retrieval_result: null });
                    }
                    // boolean to hide ajax spinner
                    this.setState({ display_spinner: false });
                },
                // asynchronous callback: ajax 'fail' promise
                (asynchStatus, asynchError) => {
                    if (asynchStatus) {
                        this.setState({ ajax_retrieval_status: asynchStatus });
                        console.log(`Error Status: ${asynchStatus}`);
                    }
                    if (asynchError) {
                        this.setState({ ajax_retrieval_error: asynchError });
                        console.log(`Error Thrown: ${asynchError}`);
                    }
                    // boolean to hide ajax spinner
                    this.setState({ display_spinner: false });
                },
                // pass ajax arguments
                ajaxArguments,
            );
        }
    }
    render() {
        // local variables
        var resultType = null;
        var resultData = null;
        var saveResults = null;

        if (
            this.props &&
            this.props.results &&
            !!this.props.results.type &&
            !!this.props.results.data
        ) {
            var resultType = this.props.results.type.toUpperCase();
            var resultData = JSON.parse(this.props.results.data);
        }

        // generate result
        if (
            this.state &&
            !!this.state.ajax_retrieval_result &&
            Object.keys(this.state.ajax_retrieval_result).length > 0
        ) {
            // local variables
            var resultData = this.state.ajax_retrieval_result;
            const status = resultData.status;

            // do not present status
            delete resultData.status;

            // generate result
            var resultList = (
                <Table responsive>
                    <thead>
                        <tr>
                            <th>#</th>
                            {
                                Object.entries(resultData).map(([item_key, value]) => (
                                    <th key={`th-${item_key}`}>{item_key}</th>
                                ))
                            }
                        </tr>
                    </thead>

                    <tbody>
                        {
                            Object.entries(resultData).map(([item_key, value]) => (
                                <tr key={`tr-${item_key}`}>{
                                    Array.isArray(value) ?
                                        <td className='sublist' key={`td-${item_key}`}>
                                            {
                                                value.map((value, index) => {value})
                                            }
                                        </td>
                                        : <td className='sublist' key={`td-${item_key}`}>
                                            {value}
                                        </td>
                                }</tr>
                            ))
                        }
                    </tbody>
                </Table>
            );
        } else if (
            resultData &&
            this.props &&
            this.props.results &&
            this.props.results.data &&
            Object.keys(resultData).length > 0
        ) {
            var resultList = (
                <Table responsive>
                    <thead>
                        <tr>
                            <th>#</th>
                            {
                                Object.entries(resultData).map(([item_key, value]) => (
                                    <th key={`th-${item_key}`}>{item_key}</th>
                                ))
                            }
                        </tr>
                    </thead>

                    <tbody>
                        {
                            Object.entries(resultData).map(([item_key, value]) => (
                                <tr key={`tr-${item_key}`}>{
                                    Array.isArray(value) ?
                                        <td className='sublist' key={`td-${item_key}`}>
                                            {
                                                value.map((value, index) => {value})
                                            }
                                        </td>
                                        : <td className='sublist' key={`td-${item_key}`}>
                                            {value}
                                        </td>
                                }</tr>
                            ))
                        }
                    </tbody>
                </Table>
            );

            var saveResults = (
                <form onSubmit={this.handleSubmit} ref='savePredictionForm'>
                    <div className='row'>
                        <div className='col-sm-9'>
                            <div className='form-group'>
                                <label className='block' htmlFor='inputSaveResult'>Save Result</label>
                                <input
                                    className='form-control fullspan mn-2'
                                    type='text'
                                    name='title'
                                    placeholder='Name your result'
                                    defaultValue=''
                                />
                            </div>
                        </div>
                        <div className='col-sm-3'>
                            <div className='form-group'>
                                <Submit cssClass='btn' />
                            </div>
                        </div>
                    </div>
                </form>
            );
        } else {
            var resultList = (
                <div className='result-list'>
                    Sorry, no results available!
                </div>
            );
        }

        // display result
        return (
            <div className='result-container'>
                <h1>{resultType} Result</h1>
                <div>
                    {resultList}
                    {saveResults}
                </div>
            </div>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default CurrentResultDisplay;
