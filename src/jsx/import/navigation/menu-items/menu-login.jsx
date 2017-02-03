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
import { loadState } from '../../redux/load-storage.jsx';
import setLogoutState from '../../redux/action/login-action.jsx';

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
            this.props === undefined &&
            this.props.username === undefined
        ) {
          // update component states
            this.setState({url: '/login'});
            this.setState({url_caption: 'Sign in'});
        }
        else if (
            this.props &&
            this.props.username &&
            this.props.username != 'anonymous'
        ) {
          // update component states
            this.setState({url: '/logout'});
            this.setState({url_caption: 'Log out'});
        }
        else if (
            loadState('username') &&
            String(loadState('username')) != 'anonymous'
        ) {
          // update component states
            this.setState({url: '/logout'});
            this.setState({url_caption: 'Log out'});

          // update redux store
            var action = setLogoutState();
            this.props.dispatch(action);
        }
        else {
          // update component states
            this.setState({url: '/login'});
            this.setState({url_caption: 'Sign in'});
        }
    },
    componentWillMount: function() {
        if (
            this.props === undefined ||
            this.props.username === undefined
        ) {
          // update component states
            this.setState({url: '/login'});
            this.setState({url_caption: 'Sign in'});
        }
        else if (
            this.props &&
            this.props.username &&
            this.props.username != 'anonymous'
        ) {
          // update component states
            this.setState({url: '/logout'});
            this.setState({url_caption: 'Log out'});
        }
        else if (
            loadState('username') &&
            String(loadState('username')) != 'anonymous'
        ) {
          // update component states
            this.setState({url: '/logout'});
            this.setState({url_caption: 'Log out'});

          // update redux store
            var action = setLogoutState();
            this.props.dispatch(action);
        }
        else {
          // update component states
            this.setState({url: '/login'});
            this.setState({url_caption: 'Sign in'});
        }
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <Link
                to={this.state.url}
                activeClassName='active'
                className='btn mn-2'
            >
                <span>{this.state.url_caption}</span>
            </Link>
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuLogin
