/**
 * model-type.jsx: append list of model types.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';
import checkValidString from './../validator/valid-string.js';
import PropTypes from 'prop-types';

class ModelType extends Component {
    // prob validation: static method, similar to class A {}; A.b = {};
    static propTypes = {
        onChange: PropTypes.shape({
            value_model_type: PropTypes.string.isRequired,
        }),
    }

    constructor() {
        super();
        this.state = {
            value_model_type: '--Select--',
        };
        this.handleModelType = this.handleModelType.bind(this);
    }

    // update 'state properties': pass property to parent component
    handleModelType(event) {
        if (checkValidString(event.target.value)) {
            this.setState({ value_model_type: event.target.value });
            this.props.onChange({ value_model_type: event.target.value });
        } else {
            this.setState({ value_model_type: '--Select--' });
        }
    }

    render() {
        // display result
        return (
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
                <option value='svm'>{'Classification'}</option>
                <option value='svr'>{'Regression'}</option>

            </select>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default ModelType;
