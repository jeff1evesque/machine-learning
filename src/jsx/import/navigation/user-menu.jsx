/**
 * user-menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import HomeLink from './menu-items/home.jsx';
import LoginLinkState from '../redux/container/link-login-container.jsx';
import LoginRegisterState from '../redux/container/link-register-container.jsx';

var UserMenu = React.createClass({
    renderContent: function() {
        if (this.props.layout == 'login') {
            return (
                <nav
                    className={'main-navigation menu-login'}
                >
                    <HomeLink />
                </nav>
            );
        }
        else if (this.props.layout == 'register') {
            return (
                <nav
                    className={'main-navigation menu-register'}
                >
                    <HomeLink />
                    <LoginLinkState />
                    <LoginRegisterState />
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
                    <LoginRegisterState />
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
