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
import MenuLogin from '../../navigation/menu-items/menu-login.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    return {
        username: state
    }
}

// pass selected properties from redux state tree to component
const MenuLoginState = connect(
    mapStateToProps
)(MenuLogin)

// indicate which class can be exported, and instantiated via 'require'
export default MenuLoginState

