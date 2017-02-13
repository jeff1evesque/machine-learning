/**
 * menu-home-container.jsx: redux store for current page layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import MenuHome from '../../navigation/menu-items/menu-home.jsx;
import setPageState from '../action/page-action.jsx;

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchPage: dispatch.bind(setPageState)
    }
}

// pass selected properties from redux state tree to component
const MenuLoginState = connect(
    null,
    mapDispatchToProps
)(MenuHome)

// indicate which class can be exported, and instantiated via 'require'
export default MenuHomeState
