/**
 * menu_register.jsx: register menu markup.
 *
 * @MenuRegister, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Link } from 'react-router'

var MenuRegister = React.createClass({
  // return state to parent component
    menuClicked: function(event) {
        this.props.onChange({menu_clicked: 'register'});
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <Link
                to='/register'
                activeClassName='active'
                className='btn btn-primary'
                onClick={this.menuClicked}
            >
                <span>Sign up</span>
            </Link>
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuRegister
