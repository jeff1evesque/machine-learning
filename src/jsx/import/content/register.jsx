/**
 * register.jsx: registration form.
 *
 * @RegisterForm, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import Spinner from '../general/spinner.jsx';
import { browserHistory } from 'react-router';
import setLoginState from '../redux/action/login.jsx';
import ajaxCaller from '../general/ajax-caller.js';
import checkValidString from '../validator/valid-string.js';
import checkValidEmail from '../validator/valid-email.js';
import checkValidPassword from '../validator/valid-password.js';

var RegisterForm = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            display_spinner: false,
            submit_registration: false,
            validated_username: false,
            validated_email: false,
            validated_password: false,
        };
    },
  // callback: used to return spinner
    getSpinner: function() {
        if (this.state.display_spinner) {
            return Spinner;
        }
        else {
            return 'span';
        }
    },
  // callback: update state signifying submitted registration
    submit_registration: function(event) {
        this.setState({submitted_registration: true});
    },
  // send form data to serverside on form submission
    handleSubmit: function(event) {
      // prevent page reload
        event.preventDefault();

      // local variables
        if (this.submit_registration) {
            var ajaxEndpoint = '/register';
            var ajaxArguments = {
                'endpoint': ajaxEndpoint,
                'data': new FormData(this.refs.registerForm)
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
    validateUsername: function(event) {
        const check = checkValidString(event.target.value) ? true : false;
        this.setState({'validated_username': check});
    },
    validateEmail: function(event) {
        const check = checkValidEmail(event.target.value) ? true : false;
        this.setState({'validated_email': check});
    },
    validatePassword: function(event) {
        const check = checkValidPassword(event.target.value) ? true : false;
        this.setState({'validated_password': check});
    },
  // triggered when 'state properties' change
    render: function() {
        var AjaxSpinner = this.getSpinner();
        var usernameClass = this.state.validated_username ?  '' : 'invalid';
        var passwordClass = this.state.validated_password ? '' : 'invalid';
        if (this.state.validated_email) {
            var emailClass = '';
            var emailNote = '';
        }
        else {
            var emailClass = 'invalid';
            var emailNote = <span className={emailClass}>
                Please provide a valid email.
            </span>;
        }

        return(
            <form onSubmit={this.handleSubmit} ref='registerForm'>
                <div className='form-group'>
                    <label className={'form-label ' + usernameClass}>Username</label>
                    <input
                        type='text'
                        name='user[login]'
                        className={'input-block ' + usernameClass}
                        placeholder='Pick a username'
                        onChange={this.validateUsername}
                    />
                    <p className={'note ' + usernameClass}>This will be your username</p>
                </div>

                <div className='form-group'>
                    <label className={'form-label ' + emailClass}>Email Address</label>
                    <input
                        type='text'
                        name='user[email]'
                        className={'input-block ' + emailClass}
                        placeholder='Your email address'
                        onChange={this.validateEmail}
                    />
                    <p className='note'>
                        You will get updates regarding account changes,
                        or activitites. This email address will not be
                        shared with anyone. {emailNote}
                    </p>
                </div>
 
                <div className='form-group'>
                    <label className={'form-label ' + passwordClass}>Password</label>
                    <input
                        type='password'
                        name='user[password]'
                        className={'input-block ' + passwordClass}
                        placeholder='Create a password'
                        onChange={this.validatePassword}
                    />
                    <p className={'note ' + usernameClass}>
                        Use at least one letter, one numeral,
                        and ten characters.
                    </p>
                </div>

                <input
                    type='submit'
                    className='btn btn-primary'
                    value='Create an account'
                    onClick={this.submit_registration}
                />
                <AjaxSpinner />
            </form>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default RegisterForm
