/**
 * user_menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import MenuHome from './menu-items/menu_home.jsx';
import MenuLoginState from '../redux/container/menu-login-container.jsx';
import MenuRegister from './menu-items/menu_register.jsx';

var UserMenu = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            show_login: true,
            show_register: true,
            page: 'home',
        };
    },
  // return state to parent, and current component
    displayHome: function(event) {
        if (event.menu_clicked == 'home') {
          // return state to parent component
            this.props.onChange({home: true});

          // display login / register buttons
            this.setState({show_login: true});
            this.setState({show_register: true});
            this.setState({page: 'home'});
        }
    },
  // return state to parent, and current component
    displayLogin: function(event) {
        if (event.menu_clicked == 'login') {
          // return state to parent component
            this.props.onChange({login: true});

          // conditionally define state(s)
            this.setState({show_login: false});
            this.setState({show_register: false});
            this.setState({page: 'login'});
        }
    },
  // return state to parent, and current component
    displayRegister: function(event) {
        if (event.menu_clicked == 'register') {
          // return state to parent component
            this.props.onChange({register: true});

          // display login / register buttons
            this.setState({show_login: true});
            this.setState({show_register: true});
            this.setState({page: 'register'});
        }
    },
  // display result
    render: function() {
        if (this.state.show_login) {
            var Login = MenuLoginState
        }
        else {
            var Login = 'span'
        }
        if (this.state.show_register) {
            var Register = MenuRegister
        }
        else {
            var Register = 'span'
        }

        return(
            <nav
                className={'main-navigation menu-' + this.state.page}
            >
                <MenuHome onChange={this.displayHome} />
                <Login onChange={this.displayLogin} />
                <Register onChange={this.displayRegister} />
            </nav>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default UserMenu
