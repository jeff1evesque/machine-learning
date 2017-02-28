/**
 * result-display.jsx: display prediction result.
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
        var result_type = 'default';
        var result_data = null;
        console.log('result-display.jsx (render): ', this.props);

        if (
            this.props &&
            this.props.results &&
            !!this.props.results.type &&
            !!this.props.results.data
        ) {
            var result_type = this.props.results.type.toUpperCase();
            var result_data = JSON.parse(this.props.results.data);
        }

      // generate result
        if (result_data && result_data.length > 0) {
            result_list.push(<ul>);
            for (var key in result_data) {
               result_list.push(<li className='result-item'>key: result_data[key]</li>);
            );
            result_list.push(</ul>)
        }
        else {
            result_list.push(
                <h3>No results available!</h3>
            );
        }

      // display result
        return(
            <div className='result-container'>
                <h1>{result_type} Prediction Result</h1>
                <div className='results'>
                    {result_list}
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ResultDisplay
