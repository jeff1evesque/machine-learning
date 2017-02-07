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
import setLoginState from '../redux/action/login-action.jsx';

var LoginForm = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            display_spinner: false,
            submit_login: false,
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
  // callback: update state signifying submitted login
    submit_login: function(event) {
        this.setState({submitted_login: true});
    },
  // send form data to serverside on form submission
    handleSubmit: function(event) {
      // prevent page reload
        event.preventDefault();

      // local variables
        if (this.submit_login) {
            var ajaxEndpoint = '/login';
            var ajaxArguments = {
                'endpoint': ajaxEndpoint,
                'data': new FormData(this.refs.loginForm)
            };

          // boolean to show ajax spinner
            this.setState({display_spinner: true});

          // asynchronous callback: ajax 'done' promise
           ajaxCaller(function (asynchObject) {

            // Append to DOM
                if (asynchObject && asynchObject.error) {
                    this.setState({ajax_done_error: asynchObject.error});
                } else if (asynchObject) {
                    this.setState({ajax_done_result: asynchObject});

                  // store into redux store logged-in state
                    if (
                        asynchObject.username &&
                        asynchObject.status === 0
                    ) {
                      // local variables
                        var username = asynchObject.username

                      // update redux store
                        var action = setLoginState(username);
                        this.props.dispatch(action);
                    }
                }
                else {
                    this.setState({ajax_done_result: null});
                }

            // boolean to hide ajax spinner
                this.setState({display_spinner: false});

            // redirect to homepage if logged-in
                if (username && username != 'anonymous') {
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
        }
    },
    componentWillMount: function() {
      // load username from redux: user already logged-in
        if (
            this.props &&
            this.props.username != 'anonymous'
        ) {
            var username = this.props.username;
        }
      // load username from sessionStorage: maybe browser reloaded
        else if (
            (this.props === undefined || this.props.username === undefined) &&
            sessionStorage.getItem('username') &&
            sessionStorage.getItem('username') != 'anonymous'
        ) {
            var username = sessionStorage.getItem('username')
            var action = setLoginState(username);
            this.props.dispatch(action);
        }
        else if (
            this.props &&
            this.props.username == 'anonymous' &&
            sessionStorage.getItem('username') &&
            sessionStorage.getItem('username') != 'anonymous'
        ) {
            var username = sessionStorage.getItem('username')
            var action = setLoginState(username);
            this.props.dispatch(action);
        }

      // redirect to homepage if logged-in
        if (username && username != 'anonymous') {
            browserHistory.push('/');
        }
    },
  // triggered when 'state properties' change
    render: function() {
        var AjaxSpinner = this.getSpinner();

        return(
            <div className='main-full-span login-form'>
                <form onSubmit={this.handleSubmit} ref='loginForm'>
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
                            onClick={this.submit_login}
                        />
                        <AjaxSpinner />
                    </div>
                </form>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default LoginForm
