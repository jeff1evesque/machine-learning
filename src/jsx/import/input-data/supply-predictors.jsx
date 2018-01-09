/**
 * supply-predictors.jss: generate correct number of input elements, based on
 *     the number of generalized features, that can be expected for the
 *     selected dataset. When values are entered in the input element, a
 *     prediction can be estimated, and returned to the front-end.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';
import checkValidFloat from './../validator/valid-float.js';
import ajaxCaller from '../general/ajax-caller.js';
import PropTypes from 'prop-types';

class SupplyPredictors extends Component {
    // prob validation: static method, similar to class A {}; A.b = {};
    static propTypes = {
        onChange: PropTypes.func.isRequired,
        selectedCollection: PropTypes.string,
    }

    constructor() {
        super();
        this.state =  {
            ajax_done_options: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null,
        };
        this.handleIntegerEntered = this.handleIntegerEntered.bind(this);
    }

    // call back: get session id(s) from server side, and append to form
    componentDidMount() {
        // variables
        this.mounted = true;

        // ajax arguments
        const ajaxEndpoint = '/retrieve-sv-features';
        const ajaxData = { 'selected-collection': this.props.selectedCollection };
        const ajaxArguments = {
            endpoint: ajaxEndpoint,
            data: JSON.stringify(ajaxData),
            contentType: 'application/json',
        };

        // asynchronous callback: ajax 'done' promise
        if (this.mounted) {
            ajaxCaller(
                (asynchObject) => {
                    // Append to DOM
                    if (asynchObject && asynchObject.error) {
                        this.setState({ ajax_done_error: asynchObject.error });
                    } else if (asynchObject) {
                        this.setState({ ajax_done_options: asynchObject });
                    }
                },
                // asynchronous callback: ajax 'fail' promise
                (asynchStatus, asynchError) => {
                    if (asynchStatus) {
                        this.setState({ ajax_fail_status: asynchStatus });
                        console.log(`Error Status: ${asynchStatus}`);
                    }
                    if (asynchError) {
                        this.setState({ ajax_fail_error: asynchError });
                        console.log(`Error Thrown: ${asynchError}`);
                    }
                },
                // pass ajax arguments
                ajaxArguments,
            );
        }
    }

    componentWillUnmount() {
        this.mounted = false;
    }

    // update 'state properties': allow parent component(s) to access properties
    handleIntegerEntered(event) {
        { /* get array of input elements, by classname */ }
        const predictors = document.getElementsByClassName('predictionInput');

        { /*
            Iterate the node list containing the supplied predictors(s). If
            input value is a valid float, store 'true', within the array.
        */ }
        const boolArray = Array.prototype.map.call(
            predictors,
            (element) => {
                if (element.value && checkValidFloat(element.value)) {
                    return true;
                }
                return false;
            },
        );

        { /* check if every element is 'true' */ }
        const datasetFlag = boolArray.every(element => element == true);

        if (datasetFlag) {
            this.props.onChange({ submitted_proper_predictor: true });
        } else {
            this.props.onChange({ submitted_proper_predictor: false });
        }
    }

    render() {
        const options = JSON.parse(this.state.ajax_done_options);

        return (
            <fieldset className='fieldset-prediction-input'>
                <legend>{'Prediction Input'}</legend>

                <div className='form-group'>
                    {/* array components require unique 'key' value */}
                    {options && options.map((value, index) => {
                        const suffix = index.toString();
                        const predictor = this.state[`value_predictor_${suffix}`];

                        return (
                            <input
                                className='form-control fullspan-b75 predictionInput'
                                defaultValue=''
                                key={index}
                                name='prediction_input[]'
                                onChange={this.handleIntegerEntered}
                                placeholder={value}
                                type='text'
                            />
                        );
                    })}
                </div>

            </fieldset>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SupplyPredictors;
