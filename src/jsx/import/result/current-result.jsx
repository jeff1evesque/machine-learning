/**
 * current-display.jsx: display current prediction result.
 *
 * @CurrentResultDisplay, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import queryString from 'query-string';
import 'core-js/modules/es7.object.entries';
import { setLayout, setContentType, setResultsButton } from '../redux/action/page.jsx';
import Submit from '../general/submit-button.jsx';
import Spinner from '../general/spinner.jsx';
import ajaxCaller from '../general/ajax-caller.js';

var CurrentResultDisplay = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            nid: null,
            computed_result: null,
            computed_type: null,
        };
    },
  // send form data to serverside on form submission
    handleSubmit: function(event) {
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
                'endpoint': ajaxEndpoint,
                'data': formData
            };
        } else {
            var formData = new FormData(this.refs.savePredictionForm);
            formData.append('status', 'no-data');

            var ajaxArguments = {
                'endpoint': ajaxEndpoint,
                'data': formData
            };
        }

      // boolean to show ajax spinner
        this.setState({display_spinner: true});

      // asynchronous callback: ajax 'done' promise
        ajaxCaller(function (asynchObject) {
        // Append to DOM
            if (asynchObject && asynchObject.error) {
                this.setState({ajax_store_error: asynchObject.error});
            } else if (asynchObject) {
                this.setState({ajax_store_result: asynchObject});

                var action = setResultsButton({'button': {'review_results': true}});
                this.props.dispatchResultsButton(action);
            } else {
                this.setState({ajax_store_result: null});
            }
        // boolean to hide ajax spinner
            this.setState({display_spinner: false});
        }.bind(this),
      // asynchronous callback: ajax 'fail' promise
        function (asynchStatus, asynchError) {
            if (asynchStatus) {
                this.setState({ajax_store_status: asynchStatus});
                console.log('Error Status: ' + asynchStatus);
            }
            if (asynchError) {
                this.setState({ajax_store_error: asynchError});
                console.log('Error Thrown: ' + asynchError);
            }
        // boolean to hide ajax spinner
            this.setState({display_spinner: false});
        }.bind(this),
      // pass ajax arguments
        ajaxArguments);
    },
  // define properties after update
    componentDidUpdate: function() {
        if (
            this.props &&
            this.props.results &&
            !!this.props.results.data &&
            !!this.props.results.type &&
            this.state.computed_result != JSON.stringify(this.props.results.data)
        ) {
            this.setState({
                computed_result: JSON.stringify(this.props.results.data),
                computed_type: this.props.results.type
            });
        }
    },
    componentWillMount: function() {
        if (
            !!this.props &&
            !!this.props.location
        ) {
            const parsed = queryString.parse(this.props.location.search);
            if (!!parsed && !!parsed.nid) {
                this.setState({nid: parsed.nid});
            }
        }

      // update redux store: define overall page layout
        const action = setLayout({'layout': 'analysis'});
        this.props.dispatchLayout(action);

        const actionContentType = setContentType({'layout': 'result'});
        this.props.dispatchContentType(actionContentType);
    },
    componentDidMount: function() {
      // execute if 'nid' defined from 'componentWillMount'
        if (this.state && !!this.state.nid) {
          // ajax arguments
            var data = new FormData();
            data.append('id_result', this.state.nid);
            const ajaxEndpoint = '/retrieve-prediction';
            const ajaxArguments = {
                'endpoint': ajaxEndpoint,
                'data': data
            };

          // boolean to show ajax spinner
            if (
                this.state &&
                !this.state.display_spinner &&
                !this.state.ajax_done_result
            ) {
                this.setState({display_spinner: true});
            }

          // asynchronous callback: ajax 'done' promise
            ajaxCaller(function (asynchObject) {
              // Append to DOM
                if (asynchObject && asynchObject.error) {
                    this.setState({ajax_retrieval_error: asynchObject.error});
                } else if (asynchObject) {
                    this.setState({ajax_retrieval_result: asynchObject});
                } else {
                    this.setState({ajax_retrieval_result: null});
                }
            // boolean to hide ajax spinner
            this.setState({display_spinner: false});
        }.bind(this),
         // asynchronous callback: ajax 'fail' promise
            function (asynchStatus, asynchError) {
                if (asynchStatus) {
                    this.setState({ajax_retrieval_status: asynchStatus});
                    console.log('Error Status: ' + asynchStatus);
                }
                if (asynchError) {
                    this.setState({ajax_retrieval_error: asynchError});
                    console.log('Error Thrown: ' + asynchError);
                }
            // boolean to hide ajax spinner
                this.setState({display_spinner: false});
            }.bind(this),
          // pass ajax arguments
            ajaxArguments);
        }
    },
    render: function() {
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

      // polyfill 'entries'
        if (!Object.entries) {
            entries.shim();
        }

      // generate result
        if (
            this.state &&
            !!this.state.ajax_retrieval_result &&
            Object.keys(this.state.ajax_retrieval_result).length > 0
        ) {
          // local variables
            var resultData = this.state.ajax_retrieval_result
            const status = resultData.status;

          // do not present status
            delete resultData.status;

          // generate result
            var resultList = <ul className='result-list'>{
                Object.entries(resultData).map(([item_key, value]) =>
                    <li key={item_key}>{item_key}: {
                        Array.isArray(value) ?
                            <ul className='sublist' key={'sublist-' + item_key}>
                                {
                                    value.map(function(value, index) {
                                        return <li key={'subitem-' + index}>{value}</li>;
                                    })
                                }
                            </ul>
                        : value
                    }
                    </li>
                )
            }</ul>;
        } else if (
            resultData &&
            this.props &&
            this.props.results &&
            this.props.results.data &&
            Object.keys(resultData).length > 0
        ) {
            var resultList = <ul className='result-list'>{
                Object.entries(resultData).map(([item_key, value]) =>
                    <li key={item_key}>{item_key}: {
                        Array.isArray(value) ?
                            <ul className='sublist' key={'sublist-' + item_key}>
                                {
                                    value.map(function(value, index) {
                                        return <li key={'subitem-' + index}>{value}</li>;
                                    })
                                }
                            </ul>
                        : value
                    }
                    </li>
                )
            }</ul>;

            var saveResults = <form onSubmit={this.handleSubmit} ref='savePredictionForm'>
                <input
                    type='text'
                    name='title'
                    placeholder='Name your result'
                    className='mn-2'
                    defaultValue=''
                />
                <Submit cssClass='btn' />
            </form>
        } else {
            var resultList = <div className='result-list'>
                Sorry, no results available!
            </div>;
        }

      // display result
        return(
            <div className='result-container'>
                <h1>{resultType} Result</h1>
                <div>
                    {resultList}
                    {saveResults}
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default CurrentResultDisplay
