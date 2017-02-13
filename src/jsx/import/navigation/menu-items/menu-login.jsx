/**
 * menu-login.jsx: login menu markup.
 *
 * @MenuLogin, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { Link } from 'react-router';
import setLoginState from '../../redux/action/login-action.jsx';
import setLogoutState from '../../redux/action/logout-action.jsx';
import setPageState from '../../redux/action/page-action.jsx';

var MenuLogin = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            url: '/login',
            url_caption: 'Sign in',
        };
    },
    componentDidUpdate: function() {
        if (
            this.props &&
            this.props.user &&
            !!this.props.user.name &&
            this.props.user.name != 'anonymous'
        ) {
          // update component states
            this.setState({
                url: '/logout',
                url_caption: 'Log out'
            });
        }
        else if (
            this.props &&
            this.props.user &&
            this.props.user.name &&
            this.props.user.name == 'anonymous'
        ) {
          // update component states
            this.setState({
                url: '/login',
                url_caption: 'Sign in'
            });
        }
        else {
          // update component states
            this.setState({
                url: '/login',
                url_caption: 'Sign in'
            });
        }
    },
    componentWillMount: function() {
        if (
            this.props &&
            this.props.user &&
            !!this.props.user.name &&
            this.props.user.name != 'anonymous'
        ) {
          // update component states
            this.setState({
                url: '/logout',
                url_caption: 'Log out'
            });
        }
        else {
          // update component states
            this.setState({
                url: '/login',
                url_caption: 'Sign in'
            });
        }
    },
    menuClicked: function(event) {
      // logout: remove username from sessionStorage
        if (
            this.props &&
            this.props.user &&
            !!this.props.user.name &&
            this.props.user.name != 'anonymous' &&
            this.state.url == '/logout'
        ) {
          // update redux store
            var register_action = setPageState({layout: 'register'});
            this.props.dispatchPage(register_action);
            var logout_action = setLogoutState();
            this.props.dispatch(logout_action);

          // remove username from sessionStorage
            sessionStorage.removeItem('username');

          // redirect to homepage if logged-out
            browserHistory.push('/');
        }
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <Link
                to={this.state.url}
                activeClassName='active'
                className='btn mn-2'
                onClick={this.menuClicked}
            >
                <span>{this.state.url_caption}</span>
            </Link>
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuLogin
