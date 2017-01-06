/**
 * menu_login.jsx: login menu markup.
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
import { connect } from 'react-redux';
import { loadState } from '../../redux/load-storage.jsx';
import setLoginState from '../../redux/action/login-action.jsx';

var MenuLogin = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            url: '/login',
            url_caption: 'Sign in',
        };
    },
  // return state to parent component
    menuClicked: function(event) {
        this.props.onChange({menu_clicked: 'login'});
    },
    componentDidMount: function() {
        if (
            loadState('username') &&
            String(loadState('username')) != 'anonymous'
        ) {
            this.setState({url: '/logout'});
            this.setState({url_caption: 'Log out'});
        }
        else {
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
                onClick={this.menuClicked}
            >
                <span>{this.state.url_caption}</span>
            </Link>
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuLogin
