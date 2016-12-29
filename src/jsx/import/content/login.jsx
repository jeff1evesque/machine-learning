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
import { connect } from 'react-redux'
import Spinner from '../general/spinner.jsx';

const LoginState = connect(
  mapStateToProps,
  mapDispatchToProps
)(LoginForm)

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
                }
                else {
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
