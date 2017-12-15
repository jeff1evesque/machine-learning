/**
 * nav-bar.jsx: secondary menu..
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { NavLink } from 'react-router-dom';
import ReviewResultsLinkState from '../redux/container/review-results-link.jsx';

const NavBar = () =>
    // display result
    (
        <div className='lcolumn'>
            <ul className='side-menu'>
                <li>
                    <NavLink
                        to='/session/data-new'
                        activeClassName='active'
                        className='menu-item'
                    >
                            Add new data
                    </NavLink>
                </li>

                <li>
                    <NavLink
                        to='/session/data-append'
                        activeClassName='active'
                        className='menu-item'
                    >
                            Append data
                    </NavLink>
                </li>

                <li>
                    <NavLink
                        to='/session/model-generate'
                        activeClassName='active'
                        className='menu-item'
                    >
                            Generate model
                    </NavLink>
                </li>

                <li>
                    <NavLink
                        to='/session/model-predict'
                        activeClassName='active'
                        className='menu-item'
                    >
                            Make prediction
                    </NavLink>
                </li>

                <li><ReviewResultsLinkState /></li>
            </ul>
        </div>
    );
// indicate which class can be exported, and instantiated via 'require'
export default NavBar;
