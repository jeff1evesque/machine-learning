/**
 * sv-kernel.jsx: append list of support vector kernels.
 *
 * @SupportVectorKernels, must be capitalized in order for reactjs to render it
 *     as a component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import checkValidString from './../validator/valid-string.js';

var SupportVectorKernels = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_kernel_type: '--Select--'
        };
    },
  // update 'state properties'
    changeKernelType: function(event){
        if (checkValidString(event.target.value)) {
            this.props.onChange({kernelType: this.state.value_kernel_type});
        }
        else {
            this.props.onChange({kernelType: null});
        }
    },
  // triggered when 'state properties' change
    render: function(){
      // display result
        return(
            <select
                name='svm_kernel_type'
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
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default SupportVectorKernels
