/**
 * support-vector.jsx: initial form.
 *
 * @SupportVector, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import ModelGenerate from '../session-type/model-generate.jsx';
import ModelPredict from '../session-type/model-predict.jsx';
import DataNew from '../session-type/data-new.jsx';
import DataAppend from '../session-type/data-append.jsx';
import Submit from '../general/submit.jsx';
import ResultDisplay from '../result/result-display.jsx';
import Spinner from '../general/spinner.jsx';
import checkValidString from '../validator/valid-string.js';

var SupportVector = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            display_spinner: false,
            ajax_done_result: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null,
        };
    },
  // callback: get session type
    getSessionType: function(type) {
        return {
            data_new: DataNew,
            data_append: DataAppend,
            model_generate: ModelGenerate,
            model_predict: ModelPredict
        }[type] || 'span';
    },
  // update 'state properties'
    changeSessionType: function(event){
      // reset value(s)
        this.setState({
            ajax_done_result: null,
        });

      // define sessionType
        if (
            event.target.value &&
            checkValidString(event.target.value) &&
            this.state.session_type_value != event.target.value &&
            this.state.session_type != this.getSessionType(event.target.value)
        ) {
            this.setState({
                session_type: this.getSessionType(event.target.value),
                session_type_value: event.target.value
            });
        }
    },
  // send form data to serverside on form submission
    handleSubmit: function(event) {
      // prevent page reload
        event.preventDefault();

      // local variables
        var sessionType = this.state.session_type_value;
        if (
            sessionType == 'data_new' ||
            sessionType == 'data_append' ||
            sessionType == 'model_generate' ||
            sessionType == 'model_predict'
        ) {
            var ajaxEndpoint = '/load-data';
            var ajaxArguments = {
                'endpoint': ajaxEndpoint,
                'data': new FormData(this.refs.analysisForm)
            };

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
        }
    },
  // define properties before mount
    componentWillMount: function() {
        this.setState({
            session_type: this.props.sessionType,
            session_type_value: this.props.sessionTypeValue
        });
    },
  // define properties after update
    componentDidUpdate: function() {
        if (
            this.props.sessionType &&
            this.state.session_type &&
            this.props.sessionType != this.state.session_type
        ) {
            this.setState({session_type: this.props.sessionType});
        }

        if (
            this.props.sessionTypeValue &&
            this.state.session_type_value &&
            this.props.sessionTypeValue != this.state.session_type_value
        ) {
            this.setState({session_type_value: this.props.sessionTypeValue});
        }
    },
  // triggered when 'state properties' change
    render: function() {
      // define components
        var Result = ResultDisplay;

      // conditionally render form submit
        var session = this.state.session_type ? this.state.session_type : null;
        var submit_button = this.state.render_submit ? Submit : null;
        var spinner = this.state.display_spinner ? Spinner : null;

        {/* return:
            @analysisForm, attribute is used within 'handleSubmit' callback
            @formResult, is accessible within child component as
                'this.props.formResult'
        */}
        return(
            <form onSubmit={this.handleSubmit} ref='analysisForm'>
                <fieldset className='fieldset-session-type'>
                    <legend>Session Type</legend>
                    <p>Choose a session type</p>
                    <select
                        name='session_type'
                        autoComplete='off'
                        onChange={this.changeSessionType}
                        value={this.state.session_type_value}
                    >
                        <option value='' defaultValue>
                            --Select--
                        </option>

                        <option value='data_new'>
                            New Data
                        </option>

                        <option value='data_append'>
                            Append Data
                        </option>

                        <option value='model_generate'>
                            Generate Model
                        </option>

                        <option value='model_predict'>
                            Make Prediction
                        </option>
                    </select>
                </fieldset>

                {session}
                {submit_button}

                <Result formResult={this.state.ajax_done_result} />
                {spinner}
            </form>
        );
    },
});

// indicate which class can be exported, and instantiated via 'require'
export default SupportVector
