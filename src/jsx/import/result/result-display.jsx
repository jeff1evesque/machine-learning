/**
 * result-display.jsx: display prediction result.
 *
 * @ResultDisplay, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import 'core-js/modules/es7.object.entries';

var ResultDisplay = React.createClass({
    render: function(){
      // local variables
        var result_type = null;
        var result_data = null;

        if (
            this.props &&
            this.props.results &&
            !!this.props.results.type &&
            !!this.props.results.data
        ) {
            var result_type = this.props.results.type.toUpperCase();
            var result_data = JSON.parse(this.props.results.data);
        }

      // polyfill 'entries'
        if (!Object.entries) {
            entries.shim();
        }

      // generate result
        if (
            this.props &&
            this.props.results &&
            this.props.results.data &&
            Object.keys(result_data).length > 0
        ) {
            var result_list = <ul className='result-list'>{
                Object.entries(result_data).map(([item_key, value]) =>
                    <li key={item_key}>{item_key}: {
                        Array.isArray(value) ?
                            <ul className='sublist' key={'sublist-' + item_key}>
                                {
                                    value.map(function(value, index) {
                                        return <li key={'subitem-' + index}>{value}</li>;
                                    })
                                }
                            </ul>
                        : value
                    }
                    </li>
                )
            }</ul>;
        }

      // display result
        return(
            <div className='result-container'>
                <h1>{result_type} Result</h1>
                <div>
                    {result_list}
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ResultDisplay
