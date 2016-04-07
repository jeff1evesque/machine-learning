/**
 * model_predict.jsx: append 'model_predict' fieldset.
 *
 * @ModelPredict, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import SupplyPredictors from '../input-data/supply_predictors.jsx';
import checkValidInt from './../validator/valid_int.js';

var ModelPredict = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            mounted: false,
            value_model_id: '--Select--',
            render_submit: false,
            ajax_done_options: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null
        };
    },
  // update 'state properties'
    changeModelId: function(event){
        var modelId = event.target.value;

        if (modelId && modelId != '--Select--' && checkValidInt(modelId)) {
            this.setState({value_model_id: event.target.value});
        }
        else {
            this.setState({value_model_id: '--Select--'});
            this.props.onChange({render_submit: false});
        }
    },
  // update 'state properties' from child component (i.e. 'validStringEntered')
    displaySubmit: function(event) {
        if (event.submitted_proper_predictor) {
            this.props.onChange({
                render_submit: event.submitted_proper_predictor
            });
        }
        else {
            this.props.onChange({render_submit: false});
        }
    },
  // triggered when 'state properties' change
    render: function(){
        var inputModelId = this.state.value_model_id;
        var Predictors = this.getSupplyPredictors(inputModelId);
        var options = this.state.ajax_done_options;

        return(
            <fieldset className='fieldset-session-predict'>
                <legend>Analysis</legend>
                <fieldset className='fieldset-dataset-type'>
                    <legend>Configurations</legend>
                    <p>Select a previous model to analyze</p>
                    <select
                        name='svm_model_id'
                        autoComplete='off'
                        onChange={this.changeModelId}
                        value={this.state.value_model_id}
                    >

                        <option value='' defaultValue>--Select--</option>

                        {/* array components require unique 'key' value */}
                        {options && options.map(function(value) {
                            return <option key={value.id} value={value.id}>
                                {value.id}: {value.title}
                            </option>;
                        })}
                    </select>
                </fieldset>

                {/*
                    'selectedModelId' is accessible within child component as
                    'this.props.selectedModelId'
                */}
                <Predictors
                    onChange={this.displaySubmit}
                    selectedModelId={this.state.value_model_id}
                />
            </fieldset>
        );
    },
  // call back: used for the above 'render' (return 'span' if undefined)
    getSupplyPredictors: function(modelId) {
        if (modelId != '--Select--' && Number(modelId)) {
            return SupplyPredictors;
        }
        else {
            return 'span';
        }
    },
  // call back: get session id(s) from server side, and append to form
    componentDidMount: function () {
      // variables
        this.setState({mounted: true});

      // ajax arguments
        var ajaxEndpoint = '/retrieve-model/';
        var ajaxArguments = {
            'endpoint': ajaxEndpoint,
            'data': null
        };

      // asynchronous callback: ajax 'done' promise
        if (this.state.mounted) {
            ajaxCaller(function (asynchObject) {
            // Append to DOM
                if (this.state.mounted) {
                    if (asynchObject && asynchObject.error) {
                        this.setState({ajax_done_error: asynchObject.error});
                    } else if (asynchObject) {
                        this.setState({ajax_done_options: asynchObject});
                    }
                }
            }.bind(this),
          // asynchronous callback: ajax 'fail' promise
            function (asynchStatus, asynchError) {
                if (this.state.mounted) {
                    if (asynchStatus) {
                        this.setState({ajax_fail_status: asynchStatus});
                        console.log('Error Status: ' + asynchStatus);
                    }
                    if (asynchError) {
                        this.setState({ajax_fail_error: asynchError});
                        console.log('Error Thrown: ' + asynchError);
                    }
                }
            }.bind(this),
          // pass ajax arguments
            ajaxArguments);
        }
    },
    componentWillUnmount() {
        this.setState({mounted: false});
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ModelPredict
