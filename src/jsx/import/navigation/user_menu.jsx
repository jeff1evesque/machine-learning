/**
 * user_menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Link } from 'react-router'
import MenuHome from './menu-items/menu_home.jsx';
import MenuLogin from './menu-items/menu_login.jsx';
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
      // return state to parent component
        this.props.onChange({home: true});

      // display login / register buttons
        this.setState({show_login: true});
        this.setState({show_register: true});
        this.setState({page: 'home'});
    },
  // return state to parent, and current component
    displayLogin: function(event) {
      // return state to parent component
        this.props.onChange({login: true});

      // conditionally define state(s)
        this.setState({show_login: false});
        this.setState({show_register: false});
        this.setState({page: 'login'});
    },
  // return state to parent, and current component
    displayRegister: function(event) {
      // return state to parent component
        this.props.onChange({register: true});

      // display login / register buttons
        this.setState({show_login: true});
        this.setState({show_register: true});
        this.setState({page: 'register'});
    },
  // display result
    render: function() {
        if (this.state.show_login) {
            var Login = MenuLogin
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

        {/* return:
            @classRegister, is accessible within child component as
                'this.props.classRegister'
            @classLogin, is accessible within child component as
                'this.props.classLogin'
        */}
        return(
            <nav
                className={'main-navigation menu-' + this.state.page}
            >
                <Link
                    to='/'
                    activeClassName='active'
                    className='icon home'
                    onClick={this.displayHome}
                >
                    <MenuHome />
                </Link>

                <Link
                    to='/login'
                    activeClassName='active'
                    className='btn mn-2'
                    onClick={this.displayLogin}
                >
                    <Login />
                </Link>

                <Link
                    to='/register'
                    activeClassName='active'
                    className='btn btn-primary'
                    onClick={this.displayRegister}
                >
                    <Register />
                </Link>
            </nav>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default UserMenu
