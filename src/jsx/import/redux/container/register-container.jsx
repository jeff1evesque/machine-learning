/**
 * register-container.jsx: redux store for general page settings, login, and
 *                         logout processes.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import RegisterForm from '../../content/register.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
  // validate username
    if (state && state.user && !!state.user.name) {
        var username = state.user.name
    }
    else {
        var username = 'anonymous'
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchPage: dispatch.bind(setPageState)
    }
}

// pass selected properties from redux state tree to component
const RegisterState = connect(
    mapStateToProps,
    mapDispatchToProps
)(RegisterForm)

// indicate which class can be exported, and instantiated via 'require'
export default RegisterState
