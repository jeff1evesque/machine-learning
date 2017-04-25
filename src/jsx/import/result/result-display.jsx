/**
 * result-display.jsx: display prediction result.
 *
 * @ResultDisplay, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import 'core-js/modules/es7.object.entries';
import Submit from '../general/submit-button.jsx';
import Spinner from '../general/spinner.jsx';
import ajaxCaller from '../general/ajax-caller.js';

var ResultDisplay = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
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
            formData.append('type', this.state.computed_type);

            var ajaxArguments = {
                'endpoint': ajaxEndpoint,
                'data': formData
            };
        }
        else {
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
                this.setState({ajax_done_error: asynchObject.error});
            } else if (asynchObject) {
                this.setState({ajax_done_result: asynchObject});
            }
            else {
                this.setState({ajax_done_result: null});
            }
        // boolean to hide ajax spinner
            this.setState({display_spinner: false});
        }.bind(this),
      // asynchronous callback: ajax 'fail' promise
        function (asynchStatus, asynchError) {
            if (asynchStatus) {
                this.setState({ajax_fail_status: asynchStatus});
                console.log('Error Status: ' + asynchStatus);
            }
            if (asynchError) {
                this.setState({ajax_fail_error: asynchError});
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
    render: function(){
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
        }
        else {
            var resultList = <div className='result-list'>Sorry, no results available!</div>;
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
export default ResultDisplay
