/**
 * current-result.jsx: current result link markup.
 *
 * @CurrentResultLink, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { NavLink } from 'react-router-dom';

const CurrentResultLink = () =>
    (
        <NavLink
            to='/session/current-result'
            activeClassName='active'
            className='btn btn-primary'
        >
            <span>Goto results</span>
        </NavLink>
    );

// indicate which class can be exported, and instantiated via 'require'
export default CurrentResultLink;
