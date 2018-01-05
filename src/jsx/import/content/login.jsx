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

import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import Spinner from '../general/spinner.jsx';
import { setLayout, setSpinner } from '../redux/action/page.jsx';
import setLoginState from '../redux/action/login.jsx';
import ajaxCaller from '../general/ajax-caller.js';

class LoginForm extends Component {
    // prob validation: static method, similar to class A {}; A.b = {};
    static propTypes = {
        dispatchLayout: PropTypes.func,
        dispatchLogin: PropTypes.func,
        dispatchSpinner: PropTypes.func,
        user: PropTypes.shape({ name: PropTypes.string.isRequired }),
    }

    // initial 'state properties'
    constructor() {
        super();
        this.state = {
            redirect_path: '/',
            ajax_done_result: null,
            display_spinner: false,
            validated_login_server: true,
            value_username: '',
        }
        this.getSpinner = this.getSpinner.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleUsername = this.handleUsername.bind(this);
    }

    componentWillMount() {
        // update redux store
        this.props.dispatchLayout(setLayout({ layout: 'login' }));
    }

    componentDidMount() {
        this.props.dispatchSpinner(setSpinner({ spinner: false }));
    }

    handleUsername(event) {
        this.setState({ value_username: event.target.value });
    }

    // send form data to serverside on form submission
    handleSubmit(event) {
        // prevent page reload
        event.preventDefault();

        // local variables
        const ajaxEndpoint = '/login';
        const ajaxArguments = {
            endpoint: ajaxEndpoint,
            data: new FormData(this.refs.loginForm),
        };

        // boolean to show ajax spinner
        this.setState({ display_spinner: true });

        // asynchronous callback: ajax 'done' promise
        ajaxCaller(
            (asynchObject) => {
                // Append to DOM
                if (asynchObject && asynchObject.error) {
                    this.setState({ ajax_done_error: asynchObject.error });
                } else if (asynchObject) {
                    // local variables
                    const result = asynchObject;
                    const status = (!!result && result.status >= 0) ? result.status : null;

                    // backend validation: server handles one error at a time
                    if (!!status || status == 0) {
                        const username = this.state.value_username;

                        switch (status) {
                        case 0:
                            // return server response
                            this.setState({ ajax_done_result: result });

                            // update validation: reset form
                            this.setState({ validated_login_server: true });

                            // boolean to hide ajax spinner
                            this.setState({ display_spinner: false });

                            // update redux store
                            const action = setLoginState(username);
                            this.props.dispatchLogin(action);

                            // store username into sessionStorage
                            sessionStorage.setItem('username', username);

                            break;
                        case 4:
                            // return server response
                            this.setState({ ajax_done_result: result });

                            // update validation
                            this.setState({ validated_login_server: false });

                            // boolean to hide ajax spinner
                            this.setState({ display_spinner: false });

                            break;
                        default:
                            // return server response
                            this.setState({ ajax_done_result: result });

                            // update validation
                            this.setState({ validated_login_server: false });

                            // boolean to hide ajax spinner
                            this.setState({ display_spinner: false });

                            break;
                        }
                    }
                }
            },
            // asynchronous callback: ajax 'fail' promise
            (asynchStatus, asynchError) => {
                if (asynchStatus) {
                    this.setState({ ajax_fail_status: asynchStatus });
                    console.log(`Error Status: ${asynchStatus}`);
                }

                if (asynchError) {
                    this.setState({ ajax_fail_error: asynchError });
                    console.log(`Error Thrown: ${asynchError}`);
                }

                // boolean to hide ajax spinner
                this.setState({ display_spinner: false });
            },
            // pass ajax arguments
            ajaxArguments,
        );
    }

    // call back: used to return spinner
    getSpinner() {
        if (this.state.display_spinner) {
            return Spinner;
        }
        return 'span';
    }

    render() {
        // local variables
        var redirect = null;
        const AjaxSpinner = this.getSpinner();

        // backend validation
        if (!this.state.validated_login_server) {
            var loginNote = (
                <div className='invalid-pop'>
                    {'Invalid user, or password.'}
                </div>);
        } else {
            var loginNote = null;
        }

        // conditionally render redirect
        if (
            this.props &&
            this.props.user &&
            !!this.props.user.name &&
            this.props.user.name != 'anonymous'
        ) {
            var redirect = <Redirect to={this.state.redirect_path} />;
        }

        return (
            <form
                onSubmit={this.handleSubmit}
                ref='loginForm'
            >
                {redirect}
                <div className='form-header'>
                    <h1>{'Sign in Web-Interface'}</h1>
                </div>
                {loginNote}
                <div className='form-body'>
                    <label>{'Username or email address'}</label>
                    <input
                        autoFocus
                        className='input-block'
                        name='user[login]'
                        onInput={this.handleUsername}
                        type='text'
                        value={this.state.value_username}
                    />
                    <label>{'Password'}</label>
                    <input
                        className='input-block'
                        name='user[password]'
                        type='password'
                    />

                    <input
                        className='input-submit btn btn-primary'
                        type='submit'
                        value='Login'
                    />
                    <AjaxSpinner />
                </div>
            </form>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default LoginForm;
