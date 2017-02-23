/**
 * result.jsx: general result layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import ResultDisplay from '../result/result-display.jsx';

var ResultLayout = React.createClass({
    render: function() {
        return(
            <div className='analysis-container'>
                <ResultDisplay />
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ResultLayout
