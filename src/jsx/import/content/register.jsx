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
import setLoginState from '../redux/action/login-action.jsx';
import setPageState from '../redux/action/page-action.jsx';

var RegisterForm = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            display_spinner: false,
            submit_registration: false,
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
      // update redux store
        var action = setPageState({layout: 'register'});
        this.props.dispatchPage(action);

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
        var AjaxSpinner = this.getSpinner();

        return(
            <div className='main-full-span register-form'>
                <h1>Create your account</h1>
                <form onSubmit={this.handleSubmit} ref='registerForm'>
                    <div className='form-group'>
                        <label className='form-label'>Username</label>
                        <input
                            type='text'
                            name='user[login]'
                            className='input-block'
                            placeholder='Pick a username'
                        />
                        <p className='note'>This will be your username</p>
                    </div>

                    <div className='form-group'>
                        <label className='form-label'>Email Address</label>
                        <input
                            type='text'
                            name='user[email]'
                            className='input-block'
                            placeholder='Your email address'
                        />
                        <p className='note'>
                            You will get updates regarding account changes,
                            or activitites. This email address will not be
                            shared with anyone.
                        </p>
                    </div>

 
                    <div className='form-group'>
                        <label className='form-label'>Password</label>
                        <input
                            type='password'
                            name='user[password]'
                            className='input-block'
                            placeholder='Create a password'
                        />
                        <p className='note'>
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
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default RegisterForm
