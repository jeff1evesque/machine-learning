/**
 * results.jsx: results link markup.
 *
 * @ResultsLink, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';

var ResultsLink = React.createClass({
    render: function(){
        <Link
            to='/session/results'
            activeClassName='active'
            className='btn mn-2'
        >
            <span>Goto results</span>
        </Link>
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ResultsLink
