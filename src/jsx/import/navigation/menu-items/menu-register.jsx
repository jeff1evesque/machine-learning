/**
 * menu-register.jsx: register menu markup.
 *
 * @MenuRegister, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Link } from 'react-router';
import { connect } from 'react-redux';
import setLoginState from '../../redux/action/login-action.jsx';

var MenuRegister = React.createClass({
  // call back: return register button
    renderContent: function() {
        if (!!this.props.username.name) {
            return (
                <Link
                    to='/register'
                    activeClassName='active'
                    className='btn btn-primary'
                >
                   <span>Sign up</span>
                </Link>
            );
        }
        else {
            return (<span />);
        }
    },
    componentDidUpdate: function() {
        if (
            !!this.props.username.name &&
            sessionStorage.getItem('username') &&
            sessionStorage.getItem('username') != 'anonymous'
        ) {
            var username = sessionStorage.getItem('username')
            var action = setLoginState(username);
            this.props.dispatch(action);
        }
        else if (
            this.props.username.name == 'anonymous' &&
            sessionStorage.getItem('username') &&
            sessionStorage.getItem('username') != 'anonymous'
        ) {
            var username = sessionStorage.getItem('username')
            var action = setLoginState(username);
            this.props.dispatch(action);
        }
    },
    componentWillMount: function() {
        if (
            !!this.props.username.name &&
            sessionStorage.getItem('username') &&
            sessionStorage.getItem('username') != 'anonymous'
        ) {
            var username = sessionStorage.getItem('username')
            var action = setLoginState(username);
            this.props.dispatch(action);
        }
        else if (
            this.props.username.name == 'anonymous' &&
            sessionStorage.getItem('username') &&
            sessionStorage.getItem('username') != 'anonymous'
        ) {
            var username = sessionStorage.getItem('username')
            var action = setLoginState(username);
            this.props.dispatch(action);
        }
    },
  // triggered when 'state properties' change
    render: function(){
        var selectedContent = this.renderContent();

        return(selectedContent);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuRegister
