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
  // initial 'state properties'
    getInitialState: function() {
        return {
            page: 'home',
        };
    },
    componentDidUpdate: function() {
        if (this.props.componentType == 'Home') {
            this.setState({page: 'home'});
        }
        else if (this.props.componentType == 'LoginLayout') {
            this.setState({page: 'login'});
        }
        else if (this.props.componentType == 'RegisterLayout') {
            this.setState({page: 'register'});
        }
    },
    componentWillMount: function() {
        if (this.props.componentType == 'Home') {
            this.setState({page: 'home'});
        }
        else if (this.props.componentType == 'LoginLayout') {
            this.setState({page: 'login'});
        }
        else if (this.props.componentType == 'RegisterLayout') {
            this.setState({page: 'register'});
        }
    },
  // return state to parent, and current component
    renderContent: function() {
        if (this.state.page == 'home') {
            return <MenuHome />;
        }
        else if (this.state.page == 'login') {
            return <MenuLoginState />;
        }
        else if (this.state.page == 'register') {
            return <MenuRegisterState />;
        }
    },
  // display result
    render: function() {
        var SelectedContent = this.renderContent();

        return(
            <nav
                className={'main-navigation menu-' + this.state.page}
            >
                {SelectedContent}
            </nav>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default UserMenu
