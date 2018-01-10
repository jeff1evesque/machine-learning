/**
 * home.jsx: home menu markup.
 *
 * @HomeLink, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { NavLink } from 'react-router-dom';
import SvgHome from '../../svg/svg-home.jsx';
import colors from '../../general/colors.js';

const HomeLink = () =>
    (
        <NavLink
            activeClassName='active'
            className='icon home'
            to='/'
        >
            <SvgHome houseColor={colors['gray-7']} />
        </NavLink>
    );

// indicate which class can be exported, and instantiated via 'require'
export default HomeLink;
