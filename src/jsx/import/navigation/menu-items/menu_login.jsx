/**
 * menu_login.jsx: login menu markup.
 *
 * @MenuLogin, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';

var MenuLogin = React.createClass({
  // triggered when 'state properties' change
    render: function(){
        return(
            <span onClick={this.clickLogin}>Sign in</span>
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuLogin
