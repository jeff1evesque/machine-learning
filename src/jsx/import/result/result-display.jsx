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
import Submit from '../general/submit-button.jsx';

var ResultDisplay = React.createClass({
  // update redux store
    saveResults: function() {
    },
    render: function(){
      // local variables
        var resultType = null;
        var resultData = null;

        if (
            this.props &&
            this.props.results &&
            !!this.props.results.type &&
            !!this.props.results.data
        ) {
            var resultType = this.props.results.type.toUpperCase();
            var resultData = JSON.parse(this.props.results.data);
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
            Object.keys(resultData).length > 0
        ) {
            var resultList = <ul className='result-list'>{
                Object.entries(resultData).map(([item_key, value]) =>
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

            var saveBtn = <Submit
                btnValue='Save results'
                onClick={this.saveResults}
                cssClass='btn'
            />;
        }

      // display result
        return(
            <div className='result-container'>
                <h1>{resultType} Result</h1>
                <div>
                    {resultList}
                    {saveBtn}
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ResultDisplay
