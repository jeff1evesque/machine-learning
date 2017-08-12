/**
 * login.jsx: login form.
 *
 * @LoginForm, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { browserHistory } from 'react-router';
import Spinner from '../general/spinner.jsx';
import setLoginState from '../redux/action/login.jsx';
import ajaxCaller from '../general/ajax-caller.js';

var LoginForm = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            ajax_done_result: null,
            display_spinner: false,
            validated_login_server: true,
        };
    },
  // call back: used to return spinner
    getSpinner: function() {
        if (this.state.display_spinner) {
            return Spinner;
        }
        else {
            return 'span';
        }
    },
  // send form data to serverside on form submission
    handleSubmit: function(event) {
      // prevent page reload
        event.preventDefault();

      // local variables
        var ajaxEndpoint = '/login';
        var ajaxArguments = {
            'endpoint': ajaxEndpoint,
            'data': new FormData(this.refs.loginForm)
        };

      // boolean to show ajax spinner
        this.setState({display_spinner: true});

      // asynchronous callback: ajax 'done' promise
        ajaxCaller(function (asynchObject) {
        // local variables
            const result = asynchObject;

        // Append to DOM
            if (asynchObject && asynchObject.error) {
                this.setState({ajax_done_error: asynchObject.error});
            }
            else if (asynchObject) {
              // local variables
                const status = (!!result && result.status >= 0) ? result.status : null;

              // backend validation: server handles one error at a time
                if (result.username && (!!status || status == 0)) {
                    switch(status) {
                        case 0:
                          // update redux store
                            var action = setLoginState(username);
                            this.props.dispatchLogin(action);

                          // store username into sessionStorage
                            sessionStorage.setItem('username', username);

                          // reset form
                            this.setState({validated_login_server: true});
                            break;
                        case 1:
                            this.setState({validated_login_server: false});
                            break;
                        case 2:
                            this.setState({validated_login_server: false});
                            break;
                        case 3:
                            this.setState({validated_login_server: false});
                            break;
                        default:
                            this.setState({validated_login_server: false});
                            break;
                    }
                }

              // return server response
                this.setState({ajax_done_result: result});
            }
            else {
                this.setState({ajax_done_result: null});
            }

          // boolean to hide ajax spinner
            this.setState({display_spinner: false});

          // redirect to homepage if logged-in
            if (!!result && !! result.username && result.username != 'anonymous') {
                browserHistory.push('/');
            }

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
    },
    componentWillMount: function() {
      // redirect to homepage if logged-in
        if (
            this.props &&
            this.props.user &&
            !!this.props.user.name &&
            this.props.user.name != 'anonymous'
        ) {
            browserHistory.push('/');
        }
    },
  // triggered when 'state properties' change
    render: function() {
      // local variables
        var AjaxSpinner = this.getSpinner();

      // backend validation
        if (!this.state.validated_login_server) {
            var loginNote = <div className='server-response invalid'>
                Invalid user, or password!
            </div>;
        }
        else {
            var loginNote = null;
        }

        return(
            <form onSubmit={this.handleSubmit} ref='loginForm'>
                {loginNote}
                <div className='form-header'>
                    <h1>Sign in Web-Interface</h1>
                </div>
                <div className='form-body'>
                    <label>Username or email address</label>
                    <input
                        type='text'
                        name='user[login]'
                        className='input-block'
                        autoFocus
                    />
                    <label>Password</label>
                    <input
                        type='password'
                        name='user[password]'
                        className='input-block'
                    />

                    <input
                        type='submit'
                        className='input-submit btn btn-primary'
                        value='Login'
                    />
                    <AjaxSpinner />
                </div>
            </form>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default LoginForm
