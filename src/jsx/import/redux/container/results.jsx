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
import ResultDisplay from '../../result/result-display.jsx';
import setResults from '../action/results.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
  // validate button
    if (
        state &&
        state.results &&
        !!state.results.type &&
        !!state.results.data
    ) {
        var result_type = state.results.type;
        var result_data = state.results.data;
    }
    else {
        var result_type = null;
        var result_data = null;
    }

  // return redux to state
    return {
        results: {
            type: result_type,
            data: result_data
        }
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchSvButton: dispatch.bind(setResults)
    }
}

// pass selected properties from redux state tree to component
const ResultState = connect(
    mapStateToProps,
    mapDispatchToProps
)(ResultDisplay)

// indicate which class can be exported, and instantiated via 'require'
export default ResultState
