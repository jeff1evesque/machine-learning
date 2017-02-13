/**
 * user-menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import MenuHomeState from '../redux/container/menu-home-container.jsx';
import MenuLoginState from '../redux/container/menu-login-container.jsx';
import MenuRegisterState from '../redux/container/menu-register-container.jsx';

var UserMenu = React.createClass({
    renderContent: function() {
        if (this.props.layout == 'login') {
            return (
                <nav
                    className={'main-navigation menu-login'}
                >
                    <MenuHomeState />
                </nav>
            );
        }
        else if (this.props.layout == 'register') {
            return (
                <nav
                    className={'main-navigation menu-register'}
                >
                    <MenuHomeState />
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
                    <MenuHomeState />
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
