/**
 * login.jsx: redux store for login, and logout processes.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { connect } from 'react-redux';
import LoginForm from '../import/content/login.jsx';

// transforms redux data store to react properties
const mapStateToProps = (state, ownProps) => {
  return {
    active: ownProps.filter === state.visibilityFilter
  }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch, ownProps) => {
  return {
    onClick: () => {
      dispatch(setVisibilityFilter(ownProps.filter))
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
