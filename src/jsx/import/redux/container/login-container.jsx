/**
 * login-container.jsx: redux store for general page settings, login, and
 *                      logout processes.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import LoginForm from '../../content/login.jsx';
import setLoginState from '../action/login-action.jsx';
import setPageState from '../action/page-action.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    return {
        user: {
            name: state.user.name
        }
        page: {
            layout: state.page.layout
        }
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchLogin: dispatch.bind(setLoginState),
        dispatchPage: dispatch.bind(setPageState)
    }
}

// pass selected properties from redux state tree to component
const LoginState = connect(
    mapStateToProps,
    mapDispatchToProps
)(LoginForm)

// indicate which class can be exported, and instantiated via 'require'
export default LoginState
