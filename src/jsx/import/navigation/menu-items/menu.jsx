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

var MenuLink = React.createClass({
  // triggered when 'state properties' change
    render: function() {
        return(
            <NavLink
                to='/'
                activeClassName='active'
                className='icon menu'
            >
                <SvgSvgNavIcon />
            </NavLink>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuLink
