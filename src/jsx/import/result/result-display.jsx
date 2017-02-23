/**
 * result-display.jsx: append form submission result.
 *
 * @ResultDisplay, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';

var ResultDisplay = React.createClass({
    render: function(){
      // local variables
        var result_list = [];
        var result_type = this.props.data.type.toUpperCase();
        var result_keys = this.props.data.result.keys;
        var result_values = this.props.data.result.values;

      // generate result
        if (
            results_keys &&
            results_values &&
            result_keys.length > 0 &&
            result_keys.length == result_values.length
        ) {
            result_keys.map((result_key, index) => {
                result_list.push(<li className='result-item'>result_key: result_values[index]</li>);
            });
        }
        else if (
            results_keys &&
            results_values &&
            (result_keys.length > 0 || result_values.length > 0) &&
            result_keys.length != result_values.length
        ) {
            result_list.push(
                <li className='result-item error'>Error: array results mismatching.</li>
            );
        }
        else if (
            results_keys &&
            results_values &&
            result_keys.length == 0 &&
            result_values.length == 0
        ) {
            result_list.push(
                <li className='result-item error'>Error: empty result returned.</li>
            );
        }
        else {
            result_list.push(
                <li className='result-item'>No results available!</li>
            );
        }

      // display result
        return(
            <div className='result-container'>
                <h1>{result_type} Prediction Result</h1>
                <ul className='result-list'>
                    {result_list}
                </ul>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ResultDisplay
