/**
 * nav-bar.jsx: secondary menu..
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { NavLink } from 'react-router-dom';
import ReviewResultsLinkState from '../redux/container/review-results-link.jsx';

const NavBar = () => (
    <div className='lcolumn'>
        <ul className='side-menu'>
            <li>
                <NavLink
                    activeClassName='active'
                    className='menu-item'
                    to='/session/data-new'
                >
                    {'Add new data'}
                </NavLink>
            </li>

            <li>
                <NavLink
                    activeClassName='active'
                    className='menu-item'
                    to='/session/data-append'
                >
                    {'Append data'}
                </NavLink>
            </li>

            <li>
                <NavLink
                    activeClassName='active'
                    className='menu-item'
                    to='/session/model-generate'
                >
                    {'Generate model'}
                </NavLink>
            </li>

            <li>
                <NavLink
                    activeClassName='active'
                    className='menu-item'
                    to='/session/model-predict'
                >
                    {'Make prediction'}
                </NavLink>
            </li>

            <li><ReviewResultsLinkState /></li>
        </ul>
    </div>
);

// indicate which class can be exported, and instantiated via 'require'
export default NavBar;
