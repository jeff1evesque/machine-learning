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
        var result = [];
        var result_type = this.props.data.type.toUpperCase();;
        var result_keys = this.props.data.result.keys;
        var result_values = this.props.data.result.values;

      // generate result
        if (result_keys.length == result_values.length) {
            result_keys.map((result_key, index) => {
                result.push(<li className='result-item'>result_key: result_values[index]</li>);
            });
        }
        else {
            result.push(<li className='result-item error'>Error: mismatch with results array)</li>);
        }

      // display result
        return(
            <div className='result-container'>
                <h1>{result_type} Prediction Result</h1>
                <ul className='result-list'>
                    {result}
                </ul>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ResultDisplay
