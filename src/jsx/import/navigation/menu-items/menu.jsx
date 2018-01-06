/**
 * user.jsx: user menu markup.
 *
 * @MenuLink, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { NavLink } from 'react-router-dom';
import SvgNavIcon from '../../svg/svg-navicon.jsx';

const MenuLink = () => (
    <NavLink
        activeClassName='active'
        className='icon menu'
        to='/'
    >
        <SvgNavIcon />
    </NavLink>
);

// indicate which class can be exported, and instantiated via 'require'
export default MenuLink;
