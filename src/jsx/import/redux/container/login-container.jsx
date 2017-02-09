/**
 * login-container.jsx: redux store for login, and logout processes.
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

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    return {
        user: state
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch, entity) => {
    return {
        dispatch: dispatch,
        user: {
            name: entity.name,
            type: entity.type,
        }
    }
}

// pass selected properties from redux state tree to component
const LoginState = connect(
    mapStateToProps,
    mapDispatchToProps
)(LoginForm)

// indicate which class can be exported, and instantiated via 'require'
export default LoginState
