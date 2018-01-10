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
import transpose from '../formatter/transpose.js';
import PropTypes from 'prop-types';

class CurrentResultDisplay extends Component {
    // prob validation: static method, similar to class A {}; A.b = {};
    static propTypes = {
        dispatchContentType: PropTypes.func,
        dispatchLayout: PropTypes.func,
        dispatchLogout: PropTypes.func,
        dispatchResultsButton: PropTypes.func,
        location: PropTypes.shape({
            search: PropTypes.string.isRequired,
        }),
        results: PropTypes.shape({
            data: PropTypes.string,
            type: PropTypes.string,
        }),
    }

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

    componentWillMount() {
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

    componentWillReceiveProps(nextProps) {
        if (
            this.props &&
            this.props.results &&
            !!this.props.results.data &&
            nextProps &&
            nextProps.results &&
            !!nextProps.results.data
        ) {
            const props_data = this.props.results;
            const next_data = nextProps.results;

            if (props_data != next_data) {
                this.setState({
                    computed_result: JSON.stringify(next_data.data),
                    computed_type: next_data.type,
                });
            }
        };
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

    tableHeaders(header) {
        var row = Object.entries(header).map(([key, value]) => (
            <th key={`th-${key}`}>{key}</th>
        ));
        return <tr><th>{'#'}</th>{row}</tr>;
    }

    tableRows(body) {
        if (Array.isArray(body)) {
            return body.map((rows, trIdx) => {
                var row = rows.map((cell, tdIdx) =>
                    <td key={`td-row${trIdx}-cell${tdIdx}`}>{cell}</td>
                );
                return <tr key={`tr-${trIdx}`}><td key={`td-index-${trIdx}`}>{trIdx}</td>{row}</tr>;
            });
        }
        else {
            var row = Object.entries(body).map(([key, value]) => (
                <td key={`td-singleton-${key}`}>{value}</td>
            ));
            return <tr><td>{'1'}</td>{row}</tr>;
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

            // destructure object
            const {result, status, ...selected} = resultData;

            // perform transpose
            const adjusted = transpose(selected);

            // generate result
            var resultList = (
                <div className='result-form'>
                    <Table
                        className='result-row'
                        responsive
                    >
                        <thead>
                            {this.tableHeaders(selected)}
                        </thead>

                        <tbody>
                            {this.tableRows(adjusted)}
                        </tbody>
                    </Table>
                    <div className='row result-row'>
                        <div className='col-sm-9 prediction-result'>
                            <h4>
                                <span className='grayed-font'>{'Predicted: '}</span>
                                {result}
                            </h4>
                        </div>
                        <div className='col-sm-3'>
                            <form
                                onSubmit={this.handleSubmit}
                                ref='savePredictionForm'
                            >
                                <div className='row'>
                                    <div className='col-sm-12'>
                                        <div className='form-group no-vertical-margin'>
                                            <input
                                                className='form-control fullspan'
                                                defaultValue=''
                                                disabled
                                                name='title'
                                                placeholder='Name your result'
                                                type='text'
                                            />
                                        </div>
                                    </div>
                                </div>
                                <div className='row'>
                                    <div className='col-sm-12'>
                                        <div className='form-group'>
                                            <Submit
                                                btnDisabled
                                                btnValue='Save'
                                                cssClass='btn fullspan'
                                            />
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            );
        } else if (
            resultData &&
            this.props &&
            this.props.results &&
            this.props.results.data &&
            Object.keys(resultData).length > 0
        ) {
            // destructure object
            const {result, ...selected} = resultData;

            // perform transpose
            const adjusted = (resultData && resultData.r2) ? selected : transpose(selected);

            var resultList = (
                <div className='result-form'>
                    <Table
                        className='result-row'
                        responsive
                    >
                        <thead>
                            {this.tableHeaders(selected)}
                        </thead>

                        <tbody>
                            {this.tableRows(adjusted)}
                        </tbody>
                    </Table>
                    <div className='row result-row'>
                        <div className='col-sm-9 prediction-result'>
                            <h4>
                                <span className='grayed-font'>{'Predicted: '}</span>
                                {result}
                            </h4>
                        </div>
                        <div className='col-sm-3'>
                            <form
                                onSubmit={this.handleSubmit}
                                ref='savePredictionForm'
                            >
                                <div className='row'>
                                    <div className='col-sm-12'>
                                        <div className='form-group no-vertical-margin'>
                                            <input
                                                className='form-control fullspan'
                                                defaultValue=''
                                                name='title'
                                                placeholder='Name your result'
                                                type='text'
                                            />
                                        </div>
                                    </div>
                                </div>
                                <div className='row'>
                                    <div className='col-sm-12'>
                                        <div className='form-group'>
                                            <Submit
                                                btnValue='Save'
                                                cssClass='btn fullspan'
                                            />
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            );
        } else {
            var resultList = (
                <div className='result-list'>
                    {'Sorry, no results available!'}
                </div>
            );
        }

        // display result
        return (
            <div className='result-container'>
                <h1>{`${resultType} Result`}</h1>
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
