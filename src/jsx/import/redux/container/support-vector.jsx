/**
 * support-vector.jsx: redux store for storing support vector analysis results.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import SupportVector from '../../content/support-vector.jsx';
import setResult from '../action/result.jsx';

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchResults: dispatch.bind(setResult)
    }
}

// pass selected properties from redux state tree to component
const SupportVectorState = connect(
    null,
    mapDispatchToProps
)(SupportVector)

// indicate which class can be exported, and instantiated via 'require'
export default SupportVectorState
