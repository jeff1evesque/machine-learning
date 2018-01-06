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
    // prob validation: static method, similar to class A {}; A.b = {};
    static propTypes = {
        dispatchContentType: PropTypes.func,
        dispatchLayout: PropTypes.func,
        dispatchSpinner: PropTypes.func,
        dispatchSvButton: PropTypes.func,
    }

    constructor() {
        super();
        this.state = {
            checked_penalty: false,
            checked_gamma: false,
            value_collection: '--Select--',
            value_model_type: '--Select--',
            value_kernel_type: '--Select--',
            ajax_done_options: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null,
        };
        this.changeCollection = this.changeCollection.bind(this);
        this.handleKernelType = this.handleKernelType.bind(this);
        this.handleModelType = this.handleModelType.bind(this);
        this.handlePenaltySlider = this.handlePenaltySlider.bind(this);
        this.handleGammaSlider = this.handleGammaSlider.bind(this);
    }

    componentWillMount() {
        // update redux store
        const actionLayout = setLayout({ layout: 'analysis' });
        this.props.dispatchLayout(actionLayout);

        const actionContentType = setContentType({ layout: 'model_generate' });
        this.props.dispatchContentType(actionContentType);
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

    componentWillUnmount() {
        // update redux store
        const action = setSvButton({ button: { submit_analysis: false } });
        this.props.dispatchSvButton(action);
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

    handleModelType(event) {
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

    handleKernelType(event) {
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

    handlePenaltySlider() {
        this.setState({
            checked_penalty: !this.state.checked_penalty
        });
    }

    handleGammaSlider() {
        this.setState({
            checked_gamma: !this.state.checked_gamma
        });
    }

    createSlider(type, min, max, step) {
        return (
            <fieldset className={`fieldset-select-${type.toLowerCase()}`}>
                <legend>{type}</legend>
                <RangeSliderState
                    max={max}
                    min={min}
                    step={step}
                />
            </fieldset>
        );
    }

    render() {
        const options = this.state.ajax_done_options;
        const penaltySlider = this.state.checked_penalty
            ? this.createSlider('Penalty', 1, 1000000, 1)
            : null;
        const gammaSlider  = this.state.checked_gamma
            ? this.createSlider('Gamma', 1, 1000, 1)
            : null;

        return (
            <fieldset className='fieldset-session-generate'>
                <fieldset className='fieldset-select-model'>
                    <legend>{'Configurations'}</legend>
                    <div className='form-group'>
                        <label
                            className='block'
                            htmlFor='selectCollection'
                        >
                            {'Collection'}
                        </label>
                        <select
                            autoComplete='off'
                            className='form-control fullspan'
                            name='collection'
                            onChange={event => this.changeCollection(event)}
                            value={this.state.value_collection}
                        >

                            <option
                                defaultValue
                                value=''
                            >
                                {'--Select--'}
                            </option>

                            {
                                options && options.map(value => (
                                    <option
                                        key={value.id}
                                        value={value.collection}
                                    >
                                        {`${value.id}: ${value.collection}`}
                                    </option>
                                )
                            )}

                        </select>
                    </div>

                    <div className='row'>
                        <div className='col-sm-6'>
                            <div className='form-group'>
                                <label
                                    className='block'
                                    htmlFor='selectModelType'
                                >
                                    {'Model Type'}
                                </label>
                                <select
                                    autoComplete='off'
                                    className='form-control fullspan'
                                    name='model_type'
                                    onChange={this.handleModelType}
                                    value={this.state.value_model_type}
                                >

                                    <option
                                        defaultValue
                                        value=''
                                    >
                                        {'--Select--'}
                                    </option>
                                    <option value='svm'>{'SVM'}</option>
                                    <option value='svr'>{'SVR'}</option>

                                </select>
                            </div>
                        </div>

                        <div className='col-sm-6'>
                            <div className='form-group'>
                                <label
                                    className='block'
                                    htmlFor='selectKernel'
                                >
                                    {'Kernel'}
                                </label>
                                <select
                                    autoComplete='off'
                                    className='form-control fullspan'
                                    name='sv_kernel_type'
                                    onChange={this.handleKernelType}
                                    value={this.state.value_kernel_type}
                                >

                                    <option
                                        defaultValue
                                        value=''
                                    >
                                        {'--Select--'}
                                    </option>
                                    <option value='linear'>{'Linear'}</option>
                                    <option value='poly'>{'Polynomial'}</option>
                                    <option value='rbf'>{'RBF'}</option>
                                    <option value='sigmoid'>{'Sigmoid'}</option>

                                </select>
                            </div>
                        </div>
                    </div>

                    <div className='row'>
                        <div className='col-sm-2'>
                            <div className='form-group'>
                                <div className='checkbox'>
                                    <label><span>{'Penalty'}</span></label>
                                    <input
                                        checked={this.state.checked_penalty}
                                        onChange={this.handlePenaltySlider}
                                        type='checkbox'
                                    />
                                </div>
                            </div>
                        </div>

                        <div className='col-sm-2'>
                            <div className='form-group'>
                                <div className='checkbox'>
                                    <label><span>{'Gamma'}</span></label>
                                    <input
                                        checked={this.state.checked_gamma}
                                        onChange={this.handleGammaSlider}
                                        type='checkbox'
                                    />
                                </div>
                            </div>
                        </div>
                    </div>
                </fieldset>
                {penaltySlider}
                {gammaSlider}
            </fieldset>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default ModelGenerate;
