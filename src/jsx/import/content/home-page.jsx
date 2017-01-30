/**
 * home-page.jsx: main homepage for entire application.
 *
 * @HomePage, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { Link } from 'react-router'

var HomePage = React.createClass({
    render: function() {
        return(
            <div className='main-full-span home'>
                <h1>Welcome!</h1>
                <Link
                    to='/session'
                    activeClassName='active'
                    className='icon home'
                    onClick={this.menuClicked}
                >
                Begin Analysis
                </Link>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default HomePage
