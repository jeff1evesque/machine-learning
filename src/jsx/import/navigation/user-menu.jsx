/**
 * user-menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import MenuHome from './menu-items/menu-home.jsx';
import MenuLoginState from '../redux/container/menu-login-container.jsx';
import MenuRegisterState from '../redux/container/menu-register-container.jsx';

var UserMenu = React.createClass({
    renderContent: function() {
        if (this.props.layout == 'login') {
            return (
                <nav
                    className={'main-navigation menu-login'}
                >
                    <MenuHome />
                </nav>
            );
        }
        else if (this.props.layout == 'register') {
            return (
                <nav
                    className={'main-navigation menu-register'}
                >
                    <MenuHome />
                    <MenuLoginState />
                    <MenuRegisterState />
                </nav>
            );
        }
        else {
            return (
                <nav
                    className={'main-navigation menu-home'}
                >
                    <MenuHome />
                    <MenuLoginState />
                    <MenuRegisterState />
                </nav>
            );
        }
    },
  // display result
    render: function() {
        var selectedContent = this.renderContent();

        return(selectedContent);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default UserMenu
