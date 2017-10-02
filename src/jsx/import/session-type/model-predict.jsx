/**
 * model-predict.jsx: append 'model_predict' fieldset.
 *
 * @ModelPredict, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 */

import React from 'react';
import SupplyPredictors from '../input-data/supply-predictors.jsx';
import checkValidString from '../validator/valid-string.js';
import Spinner from '../general/spinner.jsx';
import {
    setSvButton,
    setGotoResultsButton,
    setLayout,
    setContentType
} from '../redux/action/page.jsx';
import ajaxCaller from '../general/ajax-caller.js';

var ModelPredict = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_collection: '--Select--',
            ajax_done_options: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null
        };
    },
  // update 'state properties'
    changeCollection: function(event){
        var collection = event.target.value;

      // clear predictors, remove submit button
        var predictors = document.getElementsByClassName('predictionInput');

        if (predictors) {
            for (var i = 0; i < predictors.length; i++) {
                predictors[i].value='';
            }
        }

      // update redux store
        const analysisButton = setSvButton({button: {submit_analysis: false}});
        const gotoResultsButton = setGotoResultsButton({button: {goto_results: false}});
        this.props.dispatchSvButton(analysisButton);
        this.props.dispatchGotoResultsButton(gotoResultsButton);

      // store collection into state
        if (!!collection && collection != '--Select--' && checkValidString(collection)) {
            this.setState({value_collection: event.target.value});
        } else {
            this.setState({value_collection: '--Select--'});
        }
    },
  // update redux store
    displaySubmit: function(event) {
        if (event.submitted_proper_predictor) {
            const action = setSvButton({
                button: {submit_analysis: event.submitted_proper_predictor}
            });
            this.props.dispatchSvButton(action);
        } else {
            const action = setSvButton({button: {submit_analysis: false}});
            this.props.dispatchSvButton(action);
        }
        const gotoResultsButton = setGotoResultsButton({button: {goto_results: false}});
        this.props.dispatchGotoResultsButton(gotoResultsButton);
    },
  // triggered when 'state properties' change
    render: function(){
        var inputPredictors = null;
        const inputCollection = this.state.value_collection;
        var Predictors = this.getSupplyPredictors(inputCollection);
        if (!!Predictors) {
            var inputPredictors = <Predictors
                onChange={this.displaySubmit}
                selectedCollection={this.state.value_collection}
            />
        }
        var options = this.state.ajax_done_options;
        const spinner = !!this.state.display_spinner ? <Spinner /> : null;

        return(
            <fieldset className='fieldset-session-predict'>
                <legend>Analysis</legend>
                <fieldset className='fieldset-dataset-type'>
                    <legend>Configurations</legend>
                    <p>Select a previous model to analyze</p>
                    <select
                        name='collection'
                        autoComplete='off'
                        onChange={this.changeCollection}
                        value={this.state.value_collection}
                    >

                        <option value='' defaultValue>--Select--</option>

                        {/* array components require unique 'key' value */}
                        {options && options.map(function(value) {
                            return <option key={value.collection} value={value.collection}>
                                {value.collection}
                            </option>;
                        })}
                    </select>
                </fieldset>

                {inputPredictors}
                {spinner}
            </fieldset>
        );
    },
  // callback: used for the above 'render' (return 'span' if undefined)
    getSupplyPredictors: function(collection) {
        if (collection != '--Select--' && checkValidString(collection)) {
            return SupplyPredictors;
        } else {
            return null;
        }
    },
  // callback: get all collections from server side, and append to form
    componentDidMount: function () {
      // ajax arguments
        const ajaxEndpoint = '/retrieve-sv-model';
        const ajaxArguments = {
            'endpoint': ajaxEndpoint,
            'data': null
        };

      // boolean to show ajax spinner
        this.setState({display_spinner: true});

      // asynchronous callback: ajax 'done' promise
        ajaxCaller(function (asynchObject) {
        // Append to DOM
            if (asynchObject && asynchObject.error) {
                this.setState({ajax_done_error: asynchObject.error});
            } else if (asynchObject) {
                this.setState({ajax_done_options: asynchObject});
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
    componentWillMount: function() {
      // update redux store
        const actionLayout = setLayout({'layout': 'analysis'});
        this.props.dispatchLayout(actionLayout);

        const actionContentType = setContentType({'layout': 'model_predict'});
        this.props.dispatchContentType(actionContentType);
    },
    componentWillUnmount: function () {
      // update redux store
        const analysisButton = setSvButton({button: {submit_analysis: false}});
        const gotoResultsButton = setGotoResultsButton({button: {goto_results: false}});
        this.props.dispatchSvButton(analysisButton);
        this.props.dispatchGotoResultsButton(gotoResultsButton);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ModelPredict
