/**
 * data-append.jsx: append 'data_append' fieldset.
 *
 * @DataAppend, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * @sessionId, pass a callback to be run, within the corresponding ajax
 *     script. This allows the server side to return a list of all stored
 *     session id's, and append them to the form, respectively.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 */

import React, { Component } from 'react';
import SupplyDatasetFile from '../input-data/supply-dataset-file.jsx';
import SupplyDatasetUrl from '../input-data/supply-dataset-url.jsx';
import checkValidString from '../validator/valid-string.js';
import ModelType from '../model/model-type.jsx';
import {
    setSvButton,
    setLayout,
    setContentType,
    setSpinner
} from '../redux/action/page.jsx';
import ajaxCaller from '../general/ajax-caller.js';

class DataAppend extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state = {
            value_collection: '--Select--',
            value_dataset_type: '--Select--',
            value_model_type: '--Select--',
            ajax_done_options: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null,
        };
        this.changeCollection = this.changeCollection.bind(this);
        this.changeDatasetType = this.changeDatasetType.bind(this);
        this.changeModelType = this.changeModelType.bind(this);
        this.displaySubmit = this.displaySubmit.bind(this);
        this.getSupplyDataset = this.getSupplyDataset.bind(this);
    }
    // update 'state properties'
    changeCollection(event) {
        const collection = event.target.value;

        if (
            collection && collection != '--Select--' &&
            checkValidString(collection)
        ) {
            this.setState({ value_collection: event.target.value });
        } else {
            this.setState({ value_collection: '--Select--' });

            // update redux store
            const action = setSvButton({ button: { submit_analysis: false } });
            this.props.dispatchSvButton(action);
        }
    }
    changeDatasetType(event) {
        const datasetType = event.target.value;

        if (
            datasetType && datasetType != '--Select--' &&
            checkValidString(datasetType)
        ) {
            this.setState({ value_dataset_type: event.target.value });
        } else {
            this.setState({ value_dataset_type: '--Select--' });
        }

        // update redux store
        const action = setSvButton({ button: { submit_analysis: false } });
        this.props.dispatchSvButton(action);
    }
    // update 'state properties' from child component (i.e. 'value_model_type')
    changeModelType(event) {
        const modelType = event.value_model_type;

        if (
            modelType && modelType != '--Select--' &&
            checkValidString(modelType)
        ) {
            this.setState({ value_model_type: modelType });
        } else {
            this.setState({ value_model_type: '--Select--' });
        }

        // update redux store
        const action = setSvButton({ button: { submit_analysis: false } });
        this.props.dispatchSvButton(action);
    }
    // update 'state properties' from child component
    displaySubmit(event) {
        if (event.submitted_proper_dataset) {
            // update redux store
            const action = setSvButton({
                button: { submit_analysis: event.submitted_proper_dataset },
            });
            this.props.dispatchSvButton(action);
        } else {
            // update redux store
            const action = setSvButton({ button: { submit_analysis: false } });
            this.props.dispatchSvButton(action);
        }
    }
    // triggered when 'state properties' change
    render(sessionId) {
        const inputDatasetType = this.state.value_dataset_type;
        const inputCollection = this.state.value_collection;
        const modelType = this.state.value_model_type;
        const Dataset = this.getSupplyDataset(
            inputDatasetType,
            inputCollection,
            modelType,
        );
        const datasetInput = Dataset ? <Dataset onChange={this.displaySubmit} /> : null;
        const options = this.state.ajax_done_options;

        return (
            <fieldset className='fieldset-session-data-upload'>
                <fieldset className='fieldset-dataset-type'>
                    <legend>Configurations</legend>
                    <div className='row'>
                        <div className='col-sm-6'>
                            <div className='form-group'>
                                <label className='block' htmlFor='selectCollection'>Collection</label>
                                <select
                                    className='form-control fullspan'
                                    name='collection'
                                    autoComplete='off'
                                    onChange={this.changeCollection}
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
                        </div>

                        <div className='col-sm-6'>
                            <div className='form-group'>
                                <label className='block' htmlFor='selectDatasetType'>Dataset Type</label>
                                <select
                                    className='form-control fullspan'
                                    name='dataset_type'
                                    autoComplete='off'
                                    onChange={this.changeDatasetType}
                                    value={this.state.value_dataset_type}
                                >

                                    <option value='' defaultValue>--Select--</option>
                                    <option value='file_upload'>Upload file</option>
                                    <option value='dataset_url'>Dataset URL</option>

                                </select>
                            </div>
                        </div>
                    </div>

                    <div className='form-group'>
                        <label className='block' htmlFor='inputModelType'>Model Type</label>
                        <ModelType onChange={this.changeModelType} />
                    </div>
                </fieldset>

                {datasetInput}
            </fieldset>
        );
    }
    // call back: used for the above 'render' (return 'span' if undefined)
    getSupplyDataset(datasetType, collection, modelType) {
        if (
            datasetType && checkValidString(datasetType) &&
            datasetType != '--Select--' && collection &&
            checkValidString(collection) && modelType &&
            checkValidString(modelType) && modelType != '--Select--'
        ) {
            return {
                file_upload: SupplyDatasetFile,
                dataset_url: SupplyDatasetUrl,
            }[datasetType] || null;
        }
        return null;
    }
    // call back: get session id(s) from server side, and append to form
    componentDidMount() {
        // ajax arguments
        const ajaxEndpoint = '/retrieve-collections';
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

        const actionContentType = setContentType({ layout: 'data_append' });
        this.props.dispatchContentType(actionContentType);
    }
    componentWillUnmount() {
        // update redux store
        const action = setSvButton({ button: { submit_analysis: false } });
        this.props.dispatchSvButton(action);
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default DataAppend;
