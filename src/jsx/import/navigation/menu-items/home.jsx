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

var HomeLink = React.createClass({
  // triggered when 'state properties' change
    render: function() {
        return(
            <NavLink
                to='/'
                activeClassName='active'
                className='icon home'
            >
                <SvgHome />
            </NavLink>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default HomeLink
