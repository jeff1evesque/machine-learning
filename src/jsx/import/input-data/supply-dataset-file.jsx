/**
 * supply-dataset-file.jsx: file upload fieldset.
 *
 * @SupplyDatasetFile, must be capitalized in order for reactjs to render it as
 *     a component. Otherwise, the variable is rendered as a dom node.
 *
 * @display_submit, a boolean value, defined via '!== 0'
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';
import checkValidFile from './../validator/valid-file.js';

class SupplyDatasetFile extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state =  {
            additional_elements: [],
        };
        this.handleAddMore = this.handleAddMore.bind(this);
        this.handleRemove = this.handleRemove.bind(this);
        this.validFileEntered = this.validFileEntered.bind(this);
    }
    // update 'state properties': index for additional input elements
    handleAddMore(event) {
        const elements = this.state.additional_elements;
        elements.push(true);
        this.setState({ additional_elements: elements });
        this.props.onChange({ submitted_proper_predictor: false });
    }
    handleRemove(event) {
        const elements = this.state.additional_elements;
        let datasetBoolean = true;

        if (elements.length > 0) {
            elements.pop();
            this.setState({ additional_elements: elements });

            { /* define boolean to indicate all files properly defined */ }
            for (let index = 0; index < elements.length; index++) {
                const inputVal = this.state[`value_dataset_${index.toString()}`];

                if (inputVal === undefined || !inputVal) {
                    datasetBoolean = false;
                    return datasetBoolean;
                }
	        }

            { /* allow parent component to know all files properly defined */ }
            if (datasetBoolean) {
                this.props.onChange({ submitted_proper_dataset: true });
            } else {
                this.props.onChange({ submitted_proper_dataset: false });
            }

            { /* possibly clear submit button */ }
            this.validFileEntered();
        }
    }
    // update 'state properties': allow parent component(s) to access properties
    validFileEntered() {
        { /* get array of input elements, by classname */ }
        const dataset = document.getElementsByClassName('dataset-file');

        { /*
            Iterate the node list containing the supplied dataset(s). If the
            input value is a valid file, store 'true', within the array.
        */ }
        const boolArray = Array.prototype.map.call(dataset, (element) => {
            if (element.value && checkValidFile(element.value)) {
                return true;
            }
            return false;
        });

        { /* check if every element is 'true' */ }
        const datasetFlag = boolArray.every(element => element == true);

        if (datasetFlag) {
            this.props.onChange({ submitted_proper_dataset: true });
        } else {
            this.props.onChange({ submitted_proper_dataset: false });
        }
    }
    // triggered when 'state properties' change
    render() {
        const inputs = this.state.additional_elements;

        return (
            <fieldset className='fieldset-supply-dataset'>
                <legend>Supply Dataset</legend>

                <div className='row'>
                    <div className='col-sm-8'>
                        <div className='form-group'>
                            <input
                                type='file'
                                name='dataset[]'
                                className='dataset-file'
                                onChange={this.validFileEntered}
                                defaultValue=''
                            />
                        </div>

                        {/* array components require unique 'key' value */}
                        {inputs && inputs.map((value, index) => (
                            <div className='form-group'>
                                <input
                                    type='file'
                                    name='dataset[]'
                                    className='dataset-file'
                                    key={index}
                                    onChange={this.validFileEntered}
                                    defaultValue=''
                                />
                            </div>
                        ))}
                    </div>

                    <div className='col-sm-4'>
                        <div className='form-group'>
                            <input
                                type='button'
                                value='Add more'
                                onClick={this.handleAddMore}
                            />
                        </div>

                        <div className='form-group'>
                            <input
                                type='button'
                                value='Remove'
                                onClick={this.handleRemove}
                            />
                        </div>
                    </div>
                </div>

                <p className='form-note'>
                    <span className='asterick'>*</span>
                    <span className='bold'>Note: </span>
                    <span>Uploaded file(s) must be formatted as </span>
                    <span className='italic'>csv</span>,
                    <span className='italic'> json</span>, or
                    <span className='italic'> xml</span> format.
                </p>
            </fieldset>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SupplyDatasetFile;
