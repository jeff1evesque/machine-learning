/**
 * login.jsx: login link markup.
 *
 * @LoginLink, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { NavLink, withRouter } from 'react-router-dom';
import setLoginState from '../../redux/action/login.jsx';
import setLogoutState from '../../redux/action/logout.jsx';
import ajaxCaller from '../../general/ajax-caller.js';

var LoginLink = React.createClass({
  // call back: return login button
    renderContent: function() {
        if (
            this.props &&
            this.props.user &&
            this.props.user.name == 'anonymous'
        ) {
            return (
                <NavLink
                    to='/login'
                    activeClassName='active'
                    className='btn mn-2'
                    onClick={this.menuClicked}
                >
                    <span>Sign in</span>
                </NavLink>
            );
        } else {
            return (
                <NavLink
                    to='/logout'
                    activeClassName='active'
                    className='btn mn-2'
                    onClick={this.menuClicked}
                >
                    <span>Logout</span>
                </NavLink>
            );
        }
    },
  // logout: remove username from sessionStorage
    menuClicked: function(event) {
        if (
            this.props &&
            this.props.user &&
            !!this.props.user.name &&
            this.props.user.name != 'anonymous'
        ) {
          // prevent page reload
            event.preventDefault();

          // local variables
            var ajaxArguments = {
                'endpoint': '/logout'
            };

          // asynchronous callback: ajax 'done' promise
            ajaxCaller(function (asynchObject) {
            // Append to DOM
                if (asynchObject && asynchObject.error) {
                    this.setState({ajax_done_error: asynchObject.error});
                } else if (asynchObject) {
                    this.setState({ajax_done_result: asynchObject});

                    if (asynchObject.status == '0') {
                        var action = setLogoutState();
                        this.props.dispatchLogout(action);
                        sessionStorage.removeItem('username');
                    }

                    if (
                        this.props &&
                        this.props.location &&
                        this.props.location.pathname &&
                        this.props.location.pathname != '/' &&
                        asynchObject.status == '0'
                    ) {
                        this.props.history.push('/');
                    }
                } else {
                    this.setState({ajax_done_result: null});
                }
            // boolean to hide ajax spinner
                this.setState({display_spinner: false});
            }.bind(this),
          // asynchronous callback: ajax 'fail' promise
            function (asynchStatus, asynchError) {
                if (asynchStatus) {
                    this.setState({ajax_fail_status: asynchStatus});
                    console.log('Error Status: ' + asynchStatus);
                }
                if (asynchError) {
                    this.setState({ajax_fail_error: asynchError});
                    console.log('Error Thrown: ' + asynchError);
                }
            // boolean to hide ajax spinner
                this.setState({display_spinner: false});
            }.bind(this),
          // pass ajax arguments
            ajaxArguments);
        }
    },
    render: function(){
        var selectedContent = this.renderContent();
        return(selectedContent);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default withRouter(LoginLink)
