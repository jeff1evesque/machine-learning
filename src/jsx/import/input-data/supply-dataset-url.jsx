/**
 * supply-dataset-url.jss: url upload fieldset.
 *
 * @SupplyDatasetUrl, must be capitalized in order for reactjs to render it as
 *     a component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';
import checkValidUrl from './../validator/valid-url.js';

class SupplyDatasetUrl extends Component {
    // prob validation: static method, similar to class A {}; A.b = {};
    static propTypes = {
        onChange: PropTypes.shape({
            submitted_proper_predictor: PropTypes.bool.isRequired
        }),
    }

    constructor() {
        super();
        this.state = {
            additional_elements: [],
        };
        this.handleAddMore = this.handleAddMore.bind(this);
        this.handleRemove = this.handleRemove.bind(this);
        this.handleUrlEntered = this.handleUrlEntered.bind(this);
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

            { /* define boolean to indicate all urls properly defined */ }
            for (let index = 0; index < elements.length; index++) {
                const inputVal = this.state[`value_dataset_${index.toString()}`];
                if (inputVal === undefined || !inputVal) {
                    datasetBoolean = false;
                }
            }

            { /* allow parent component to know all files properly defined */ }
            if (datasetBoolean) {
                this.props.onChange({ submitted_proper_dataset: true });
            } else {
                this.props.onChange({ submitted_proper_dataset: false });
            }

            { /* possibly clear submit button */ }
            this.handleUrlEntered();
        }
    }

    // update 'state properties': allow parent component(s) to access properties
    handleUrlEntered() {
        { /* get array of input elements, by classname */ }
        const dataset = document.getElementsByClassName('dataset-url');

        { /*
            Iterate the node list containing the supplied dataset(s). If the
            input value is a valid file, store 'true', within the array.
        */ }
        const boolArray = Array.prototype.map.call(dataset, (element) => {
            if (element.value && checkValidUrl(element.value)) {
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

    render() {
        const inputs = this.state.additional_elements;
        return (
            <fieldset className='fieldset-supply-dataset'>
                <legend>{'Supply Dataset'}</legend>
                <div className='row'>
                    <div className='col-sm-6'>
                        <div className='form-group'>
                            <input
                                className='form-control dataset-url'
                                defaultValue=''
                                name='dataset[]'
                                onChange={this.handleUrlEntered}
                                placeholder='Dataset URL'
                                type='url'
                            />
                        </div>

                        {/* array components require unique 'key' value */}
                        {inputs && inputs.map((value, index) => (
                            <div
                                className='form-group'
                                key={`form-group-${index}`}
                            >
                                <input
                                    className='form-control dataset-url'
                                    defaultValue=''
                                    key={`input-url-${index}`}
                                    name='dataset[]'
                                    onChange={this.handleUrlEntered}
                                    placeholder='Dataset URL'
                                    type='url'
                                />
                            </div>
                        ))}
                    </div>

                    <div className='col-sm-6'>
                        <div className='row'>
                            <div className='col-sm-6 form-group'>
                                <input
                                    className='fullspan'
                                    onClick={this.handleAddMore}
                                    type='button'
                                    value='Add more'
                                />
                            </div>

                            <div className='col-sm-6 form-group'>
                                <input
                                    className='fullspan'
                                    onClick={this.handleRemove}
                                    type='button'
                                    value='Remove'
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </fieldset>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SupplyDatasetUrl;
