/**
 * model-generate.jsx: append 'model_generate' fieldset.
 *
 * @ModelGenerate, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 */

import React, { Component } from 'react';
import checkValidString from '../validator/valid-string.js';
import {
    setSvButton,
    setLayout,
    setContentType,
    setRangeSlider,
    setSpinner
} from '../redux/action/page.jsx';
import { FormGroup, Checkbox } from 'react-bootstrap';
import ajaxCaller from '../general/ajax-caller.js';
import RangeSliderState from '../redux/container/range-slider.jsx';

class ModelGenerate extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state = {
            checked_penalty: false,
            value_collection: '--Select--',
            value_model_type: '--Select--',
            value_kernel_type: '--Select--',
            ajax_done_options: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null,
        };
        this.changeCollection = this.changeCollection.bind(this);
        this.changeKernelType = this.changeKernelType.bind(this);
        this.changeModelType = this.changeModelType.bind(this);
        this.showPenaltySlider = this.showPenaltySlider.bind(this);
    }
    // update 'state properties'
    changeCollection(event) {
        const collection = event.target.value;
        const modelType = this.state.value_model_type;
        const kernelType = this.state.value_kernel_type;

        if (
            collection &&
            collection != '--Select--' &&
            checkValidString(collection)
        ) {
            this.setState({ value_collection: collection });

            // update redux store
            if (
                modelType != '--Select--' &&
                kernelType != '--Select--' &&
                checkValidString(modelType) &&
                checkValidString(kernelType)
            ) {
                const action = setSvButton({ button: { submit_analysis: true } });
                this.props.dispatchSvButton(action);
            } else {
                const action = setSvButton({ button: { submit_analysis: false } });
                this.props.dispatchSvButton(action);
            }
        } else {
            this.setState({ value_collection: '--Select--' });

            // update redux store
            const action = setSvButton({ button: { submit_analysis: false } });
            this.props.dispatchSvButton(action);
        }
    }
    changeModelType(event) {
        const collection = this.state.value_collection;
        const modelType = event.target.value;
        const kernelType = this.state.value_kernel_type;

        if (
            modelType &&
            modelType != '--Select--' &&
            checkValidString(modelType)
        ) {
            this.setState({ value_model_type: event.target.value });

            // update redux store
            if (
                checkValidString(collection) &&
                kernelType != '--Select--' &&
                checkValidString(kernelType)
            ) {
                const action = setSvButton({ button: { submit_analysis: true } });
                this.props.dispatchSvButton(action);
            } else {
                const action = setSvButton({ button: { submit_analysis: false } });
                this.props.dispatchSvButton(action);
            }
        } else {
            this.setState({ value_model_type: '--Select--' });

            // update redux store
            const action = setSvButton({ button: { submit_analysis: false } });
            this.props.dispatchSvButton(action);
        }
    }
    changeKernelType(event) {
        const collection = this.state.value_collection;
        const modelType = this.state.value_model_type;
        const kernelType = event.target.value;

        if (
            kernelType &&
            kernelType != '--Select--' &&
            checkValidString(kernelType)
        ) {
            this.setState({ value_kernel_type: event.target.value });

            // update redux store
            if (
                checkValidString(collection) &&
                modelType != '--Select--' &&
                checkValidString(modelType)
            ) {
                const action = setSvButton({ button: { submit_analysis: true } });
                this.props.dispatchSvButton(action);
            } else {
                const action = setSvButton({ button: { submit_analysis: false } });
                this.props.dispatchSvButton(action);
            }
        } else {
            this.setState({ value_kernel_type: '--Select--' });

            // update redux store
            const action = setSvButton({ button: { submit_analysis: false } });
            this.props.dispatchSvButton(action);
        }
    }
    showPenaltySlider() {
        this.setState({
            checked_penalty: !this.state.checked_penalty
        });
    }
    // triggered when 'state properties' change
    render() {
        const options = this.state.ajax_done_options;
        const penaltySlider = this.state.checked_penalty ?
            <fieldset className='fieldset-select-penalty'>
                <legend>Penalty</legend>
                <RangeSliderState step={0.1}/>
            </fieldset>
            : null;

        return (
            <fieldset className='fieldset-session-generate'>
                <fieldset className='fieldset-select-model'>
                    <legend>Configurations</legend>
                    <div className='form-group'>
                        <label className='block' htmlFor='selectCollection'>Collection</label>
                        <select
                            className='form-control fullspan'
                            name='collection'
                            autoComplete='off'
                            onChange={event => this.changeCollection(event)}
                            value={this.state.value_collection}
                        >

                            <option value='' defaultValue>--Select--</option>

                            {/* array components require unique 'key' value */}
                            {options && options.map(value =>
                                (<option key={value.id} value={value.collection}>
                                {value.id}: {value.collection}
                            </option>))}

                        </select>
                    </div>

                    <div className='row'>
                        <div className='col-sm-6'>
                            <div className='form-group'>
                                <label className='block' htmlFor='selectModelType'>Model Type</label>
                                <select
                                    className='form-control fullspan'
                                    name='model_type'
                                    autoComplete='off'
                                    onChange={this.changeModelType}
                                    value={this.state.value_model_type}
                                >

                                    <option value='' defaultValue>--Select--</option>
                                    <option value='svm'>SVM</option>
                                    <option value='svr'>SVR</option>

                                </select>
                            </div>
                        </div>

                        <div className='col-sm-6'>
                            <div className='form-group'>
                                <label className='block' htmlFor='selectKernel'>Kernel</label>
                                <select
                                    className='form-control fullspan'
                                    name='sv_kernel_type'
                                    autoComplete='off'
                                    onChange={this.changeKernelType}
                                    value={this.state.value_kernel_type}
                                >

                                    <option value='' defaultValue>--Select--</option>
                                    <option value='linear'>Linear</option>
                                    <option value='poly'>Polynomial</option>
                                    <option value='rbf'>RBF</option>
                                    <option value='sigmoid'>Sigmoid</option>

                                </select>
                            </div>
                        </div>
                    </div>

                    <div className='form-group'>
                        <div className='checkbox'>
                            <label><span>Penalty</span></label>
                            <input
                                type='checkbox'
                                checked={this.state.checked_penalty}
                                onChange={this.showPenaltySlider}
                            />
                        </div>
                    </div>
                </fieldset>
                {penaltySlider}
            </fieldset>
        );
    }
    // call back: get all collections from server side, and append to form
    componentDidMount() {
        // ajax arguments
        const ajaxEndpoint = '/retrieve-collections';
        const ajaxArguments = {
            endpoint: ajaxEndpoint,
            data: null,
        };

        // boolean to show ajax spinner
        var action = setSpinner({'spinner': false});
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
                    console.log(`Error Status: ${asynchStatus}`);
                }
                if (asynchError) {
                    this.setState({ ajax_fail_error: asynchError });
                    console.log(`Error Thrown: ${asynchError}`);
                }
                // boolean to hide ajax spinner
                var action = setSpinner({'spinner': false});
                this.props.dispatchSpinner(action);
            },
            // pass ajax arguments
            ajaxArguments,
        );
    }
    componentWillMount() {
        // update redux store
        const actionLayout = setLayout({ layout: 'analysis' });
        this.props.dispatchLayout(actionLayout);

        const actionContentType = setContentType({ layout: 'model_generate' });
        this.props.dispatchContentType(actionContentType);
    }
    componentWillUnmount() {
        // update redux store
        const action = setSvButton({ button: { submit_analysis: false } });
        this.props.dispatchSvButton(action);
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default ModelGenerate;
