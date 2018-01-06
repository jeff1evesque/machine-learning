/**
 * data-new.jsx: append 'data_new' fieldset.
 *
 * @DataNew, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
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
import { setSvButton, setLayout, setContentType } from '../redux/action/page.jsx';

class DataNew extends Component {
    // prob validation: static method, similar to class A {}; A.b = {};
    static propTypes = {
        dispatchContentType: PropTypes.func,
        dispatchLayout: PropTypes.func,
        dispatchSvButton: PropTypes.func,
    }

    constructor() {
        super();
        this.state = {
            value_title: '',
            value_collection: '',
            value_dataset_type: '--Select--',
            value_model_type: '--Select--',
        };
        this.changeCollection = this.changeCollection.bind(this);
        this.handleDatasetType = this.handleDatasetType.bind(this);
        this.handleModelType = this.handleModelType.bind(this);
        this.handleTitle = this.handleTitle.bind(this);
        this.getSupplyDataset = this.getSupplyDataset.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    // update 'state properties'
    handleDatasetType(event) {
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
    handleTitle(event) {
        const sessionTitle = event.target.value;

        if (sessionTitle && checkValidString(sessionTitle)) {
            this.setState({ value_title: sessionTitle });
        } else {
            this.setState({ value_title: '' });
        }

        // update redux store
        const action = setSvButton({ button: { submit_analysis: false } });
        this.props.dispatchSvButton(action);
    }
    changeCollection(event) {
        const collection = event.target.value;

        if (collection && checkValidString(collection)) {
            this.setState({ value_collection: collection });
        } else {
            this.setState({ value_collection: '' });
        }

        // update redux store
        const action = setSvButton({ button: { submit_analysis: false } });
        this.props.dispatchSvButton(action);
    }
    // update 'state properties' from child component (i.e. 'value_model_type')
    handleModelType(event) {
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
    handleSubmit(event) {
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
    componentWillMount(event) {
        // update redux store
        const actionLayout = setLayout({ layout: 'analysis' });
        this.props.dispatchLayout(actionLayout);

        const actionContentType = setContentType({ layout: 'data_new' });
        this.props.dispatchContentType(actionContentType);
    }
    // triggered when 'state properties' change
    render() {
        const datasetType = this.state.value_dataset_type;
        const datasetTitle = this.state.value_title;
        const collection = this.state.value_collection;
        const modelType = this.state.value_model_type;
        const Dataset = this.getSupplyDataset(
            datasetType,
            datasetTitle,
            collection,
            modelType,
        );
        const datasetInput = Dataset ? <Dataset onChange={this.handleSubmit} /> : null;

        return (
            <fieldset className='fieldset-session-data-upload'>
                <fieldset className='fieldset-dataset-type'>
                    <legend>{'Configurations'}</legend>
                    <div className='form-group'>
                        <label
                            className='block'
                            htmlFor='inputSessionName'
                        >
                            {'Session Name'}
                        </label>
                        <input
                            className='form-control fullspan'
                            name='session_name'
                            onInput={this.handleTitle}
                            placeholder='Session Name'
                            type='text'
                            value={this.state.value_title}
                        />
                    </div>

                    <div className='form-group'>
                        <label
                            className='block'
                            htmlFor='inputCollection'
                        >
                            {'Collection'}
                        </label>
                        <input
                            className='form-control fullspan'
                            name='collection'
                            onInput={this.changeCollection}
                            placeholder='Collection'
                            type='text'
                            value={this.state.value_collection}
                        />
                    </div>

                    <div className='row'>
                        <div className='col-sm-6'>
                            <div className='form-group'>
                                <label htmlFor='selectDatasetType'>
                                    {'Dataset Type'}
                                </label>
                                <select
                                    autoComplete='off'
                                    className='form-control fullspan'
                                    name='dataset_type'
                                    onChange={this.handleDatasetType}
                                    value={this.state.value_dataset_type}
                                >

                                    <option
                                        defaultValue
                                        value=''
                                    >
                                        {'--Select--'}
                                    </option>
                                    <option value='file_upload'>{'Upload file'}</option>
                                    <option value='dataset_url'>{'Dataset URL'}</option>
                                </select>
                            </div>
                        </div>

                        <div className='col-sm-6'>
                            <div className='form-group'>
                                <label htmlFor='inputModelType'>{'Model Type'}</label>
                                <ModelType onChange={this.handleModelType} />
                            </div>
                        </div>
                    </div>
                </fieldset>

                {datasetInput}
            </fieldset>
        );
    }
    // call back: used for the above 'render' (return 'span' if undefined)
    getSupplyDataset(datasetType, title, collection, modelType) {
        if (
            title &&
            checkValidString(title) &&
            collection &&
            checkValidString(collection) &&
            datasetType &&
            checkValidString(datasetType) &&
            datasetType != '--Select--' &&
            modelType &&
            checkValidString(modelType) &&
            modelType != '--Select--'
        ) {
            return {
                file_upload: SupplyDatasetFile,
                dataset_url: SupplyDatasetUrl,
            }[datasetType] || null;
        }
        return null;
    }
    componentWillUnmount() {
        // update redux store
        const action = setSvButton({ button: { submit_analysis: false } });
        this.props.dispatchSvButton(action);
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default DataNew;
