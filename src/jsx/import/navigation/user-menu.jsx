/**
 * user-menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import HomeLink from './menu-items/home.jsx';
import LoginLinkState from '../redux/container/login-link.jsx';
import RegisterLinkState from '../redux/container/register-link.jsx';

var UserMenu = React.createClass({
    renderContent: function() {
        if (this.props.layout.type == 'login') {
            return (
                <nav
                    className={'main-navigation menu-login'}
                >
                    <HomeLink />
                </nav>
            );
        }
        else if (this.props.layout.type == 'register') {
            return (
                <nav
                    className={'main-navigation menu-register'}
                >
                    <HomeLink />
                    <LoginLinkState />
                    <RegisterLinkState />
                </nav>
            );
        }
        else {
            return (
                <nav
                    className={'main-navigation menu-home'}
                >
                    <HomeLink />
                    <LoginLinkState />
                    <RegisterLinkState />
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
