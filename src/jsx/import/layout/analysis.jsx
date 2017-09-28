/**
 * analysis.jsx: general analysis layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import { Route } from 'react-router-dom';
import NavBar from '../navigation/nav-bar.jsx';
import DataNewState from '../redux/container/data-new.jsx';
import DataAppendState from '../redux/container/data-append.jsx';
import ModelGenerateState from '../redux/container/model-generate.jsx';
import ModelPredictState from '../redux/container/model-predict.jsx';
import SupportVectorState from '../redux/container/support-vector.jsx';
import CurrentResultState from '../redux/container/current-result.jsx';
import ResultsDisplayState from '../redux/container/results.jsx';
import ajaxCaller from '../general/ajax-caller.js';

var AnalysisLayout = React.createClass({
    getSessionType: function(type) {
        return {
            data_new: DataNewState,
            data_append: DataAppendState,
            model_generate: ModelGenerateState,
            model_predict: ModelPredictState
        }[type] || 'span';
    },
  // send form data to serverside on form submission
    handleSubmit: function(event) {
      // prevent page reload
        event.preventDefault();

      // local variables
        var sessionType = this.props.page.content_type;
        if (
            sessionType == 'data_new' ||
            sessionType == 'data_append' ||
            sessionType == 'model_generate' ||
            sessionType == 'model_predict'
        ) {
            const ajaxEndpoint = '/load-data';
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
                    this.storeResults();
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
    render: function() {
      // determine content
        var sessionType = this.props.page.content_type;
        var content = this.getSessionType(sessionType);

        if (sessionType == 'result') {
            var display_content = content;
        }
        else if (!!sessionType) {
            var display_content = <SupportVectorState
                sessionType={content}
                sessionTypeValue={sessionType}
            />;
        }
        else {
            var display_content = this.props.children;
        }

        {/* return:
            @analysisForm, attribute is used within 'handleSubmit' callback
            @formResult, is accessible within child component as
                'this.props.formResult'
        */}
        return(
            <div>
                <NavBar />
                <form onSubmit={this.handleSubmit} ref='analysisForm'>
                    <Route
                        exact
                        path='/session/data-new'
                        component={DataNewState}
                    />
                    <Route
                        exact
                        path='/session/data-append'
                        component={DataAppendState}
                    />
                    <Route
                        exact
                        path='/session/model-generate'
                        component={ModelGenerateState}
                    />
                    <Route
                        exact
                        path='/session/model-predict'
                        component={ModelPredictState}
                    />
                    <Route
                        exact
                        path='/session/current-result'
                        component={CurrentResultState}
                    />
                </form>
                <Route
                    exact
                    path='/session/results'
                    component={ResultsDisplayState}
                />
                <div className='analysis-container'>
                    {display_content}
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default AnalysisLayout
