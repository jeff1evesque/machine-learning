/**
 * results.jsx: redux store for analysis results.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import ResultsDisplay from '../../result/current-result.jsx';
import { setContentType } from '../action/page.jsx';

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchContentType: dispatch.bind(setContentType)
    }
}

// pass selected properties from redux state tree to component
const ResultsDisplayState = connect(
    null,
    mapDispatchToProps
)(ResultsDisplay)

// indicate which class can be exported, and instantiated via 'require'
export default ResultsDisplayState
