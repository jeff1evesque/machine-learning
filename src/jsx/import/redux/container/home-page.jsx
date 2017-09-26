/**
 * current-result.jsx: redux store for analysis results.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import HomePage from '../../content/home-page.jsx';
import { setLayout } from '../action/page.jsx';

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchLayout: dispatch.bind(setLayout)
    }
}

// pass selected properties from redux state tree to component
const HomePageState = connect(
    null,
    mapDispatchToProps
)(HomePage)

// indicate which class can be exported, and instantiated via 'require'
export default HomePageState
