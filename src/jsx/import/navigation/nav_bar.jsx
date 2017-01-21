/**
 * navbar.jsx: secondary menu..
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Link } from 'react-router'

var NavBar = React.createClass({
  // display result
    render: function() {
        return(
            <div className='menu-container'>
                <ul className='side-menu'>
                    <li>
                        <Link
                           to='/session/data-new'
                           activeClassName='active'
                           className='menu-item'
                        >
                            Add new data
                        </Link>
                    </li>

                    <li>
                        <Link
                            to='/session/data-append'
                            activeClassName='active'
                            className='menu-item'
                        >
                            Append data
                        </Link>
                    </li>

                    <li>
                        <Link
                            to='/session/model-generate'
                            activeClassName='active'
                            className='menu-item'
                        >
                            Generate model
                        </Link>
                    </li>

                    <li>
                        <Link
                            to='/session/model-predict'
                            activeClassName='active'
                            className='menu-item'
                        >
                            Make prediction
                        </Link>
                    </li>
                </ul>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default NavBar
