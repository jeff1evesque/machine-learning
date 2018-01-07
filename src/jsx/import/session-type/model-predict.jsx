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

import React, { Component } from 'react';
import SupplyPredictors from '../input-data/supply-predictors.jsx';
import checkValidString from '../validator/valid-string.js';
import {
    setSvButton,
    setGotoResultsButton,
    setLayout,
    setContentType,
    setSpinner
} from '../redux/action/page.jsx';
import ajaxCaller from '../general/ajax-caller.js';
import PropTypes from 'prop-types';

class ModelPredict extends Component {
    // prob validation: static method, similar to class A {}; A.b = {};
    static propTypes = {
        dispatchContentType: PropTypes.func,
        dispatchGotoResultsButton: PropTypes.func,
        dispatchLayout: PropTypes.func,
        dispatchSpinner: PropTypes.func,
        dispatchSvButton: PropTypes.func,
    }

    constructor() {
        super();
        this.state = {
            value_collection: '--Select--',
            ajax_done_options: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null,
        };
        this.handleCollection = this.handleCollection.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.getSupplyPredictors = this.getSupplyPredictors.bind(this);
    }

    componentWillMount() {
        // update redux store
        const actionLayout = setLayout({ layout: 'analysis' });
        this.props.dispatchLayout(actionLayout);

        const actionContentType = setContentType({ layout: 'model_predict' });
        this.props.dispatchContentType(actionContentType);
    }

    // callback: get all collections from server side, and append to form
    componentDidMount() {
        // ajax arguments
        const ajaxEndpoint = '/retrieve-sv-model';
        const ajaxArguments = {
            endpoint: ajaxEndpoint,
            data: null,
        };

        // boolean to show ajax spinner
        var action = setSpinner({'spinner': true});
        this.props.dispatchSpinner(action);

        // asynchronous callback: ajax 'done' promise
        ajaxCaller(
            (asynchObject) => {
                // Append to DOM
                if (asynchObject && asynchObject.error) {
                    this.setState({ ajax_done_error: asynchObject.error });
                } else if (asynchObject) {
                    this.setState({ ajax_done_options: asynchObject });
                }
                // boolean to hide ajax spinner
                var action = setSpinner({'spinner': false});
                this.props.dispatchSpinner(action);
            },
            // asynchronous callback: ajax 'fail' promise
            (asynchStatus, asynchError) => {
                if (asynchStatus) {
                    this.setState({ ajax_fail_status: asynchStatus });
                    console.log(`Error Status: ${  asynchStatus}`);
                }
                if (asynchError) {
                    this.setState({ ajax_fail_error: asynchError });
                    console.log(`Error Thrown: ${  asynchError}`);
                }
                // boolean to hide ajax spinner
                var action = setSpinner({'spinner': false});
                this.props.dispatchSpinner(action);
            },
            // pass ajax arguments
            ajaxArguments,
        );
    }

    componentWillUnmount() {
        // update redux store
        const analysisButton = setSvButton({ button: { submit_analysis: false } });
        const gotoResultsButton = setGotoResultsButton({ button: { goto_results: false } });
        this.props.dispatchSvButton(analysisButton);
        this.props.dispatchGotoResultsButton(gotoResultsButton);
    }

    handleCollection(event) {
        const collection = event.target.value;

        // clear predictors, remove submit button
        const predictors = document.getElementsByClassName('predictionInput');

        if (predictors) {
            for (let i = 0; i < predictors.length; i++) {
                predictors[i].value = '';
            }
        }

        // update redux store
        const analysisButton = setSvButton({ button: { submit_analysis: false } });
        const gotoResultsButton = setGotoResultsButton({ button: { goto_results: false } });
        this.props.dispatchSvButton(analysisButton);
        this.props.dispatchGotoResultsButton(gotoResultsButton);

        // store collection into state
        if (!!collection && collection != '--Select--' && checkValidString(collection)) {
            this.setState({ value_collection: event.target.value });
        } else {
            this.setState({ value_collection: '--Select--' });
        }
    }

    handleSubmit(event) {
        if (event.submitted_proper_predictor) {
            const action = setSvButton({
                button: { submit_analysis: event.submitted_proper_predictor },
            });
            this.props.dispatchSvButton(action);
        } else {
            const action = setSvButton({ button: { submit_analysis: false } });
            this.props.dispatchSvButton(action);
        }
        const gotoResultsButton = setGotoResultsButton({ button: { goto_results: false } });
        this.props.dispatchGotoResultsButton(gotoResultsButton);
    }

    getSupplyPredictors(collection) {
        if (collection != '--Select--' && checkValidString(collection)) {
            return SupplyPredictors;
        }
        return null;
    }

    render() {
        var inputPredictors = null;
        const inputCollection = this.state.value_collection;
        const Predictors = this.getSupplyPredictors(inputCollection);
        if (Predictors) {
            var inputPredictors = (
                <Predictors
                    onChange={this.handleSubmit}
                    selectedCollection={this.state.value_collection}
                />
            );
        }
        const options = this.state.ajax_done_options;

        return (
            <fieldset className='fieldset-session-predict'>
                <fieldset className='fieldset-dataset-type'>
                    <legend>{'Configurations'}</legend>
                    <div className='form-group'>
                        <select
                            autoComplete='off'
                            className='form-control fullspan'
                            name='collection'
                            onChange={this.handleCollection}
                            value={this.state.value_collection}
                        >

                            <option
                                defaultValue
                                value=''
                            >
                                {'--Select--'}
                            </option>

                            {
                                options && options.map((value) => (
                                    <option
                                        key={value.collection}
                                        value={value.collection}
                                    >
                                        {value.collection}
                                    </option>
                                ))
                            }
                        </select>
                    </div>
                </fieldset>

                {inputPredictors}
            </fieldset>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default ModelPredict;
