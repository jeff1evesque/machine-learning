/**
 * menu_register.jsx: register menu markup.
 *
 * @MenuRegister, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';

var MenuRegister = React.createClass({
  // triggered when 'state properties' change
    render: function(){
        return(
            <span onClick={this.clickRegister}>Sign up</span>
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuRegister
