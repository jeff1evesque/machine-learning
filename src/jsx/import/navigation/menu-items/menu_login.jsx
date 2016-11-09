/**
 * menu_login.jsx: login menu markup.
 *
 * @MenuLogin, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Link } from 'react-router'

var MenuLogin = React.createClass({
  // return state to parent component
    menuClicked: function(event) {
        this.props.onChange({menu_clicked: 'login'});
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <Link
                to='/login'
                activeClassName='active'
                className='btn mn-2'
                onClick={this.menuClicked}
            >
                <span>Sign in</span>
            </Link>
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuLogin
