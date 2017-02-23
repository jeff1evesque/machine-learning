/**
 * result.jsx: redux store for analysis results.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import ResultLayout from '../../layout/result.jsx';
import setResult from '../action/result.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
  // validate button
    if (
        state &&
        state.result &&
        !!state.result.type &&
        state.result.data &&
        !!state.result.data.keys &&
        !!state.result.data.values
    ) {
        var result_type = state.result.type;
        var result_keys = state.result.data.keys;
        var result_values = state.result.data.values;
    }
    else {
        var result_type = null;
        var result_keys = null;
        var result_values = null;
    }

  // return redux to state
    return {
        result: {
            type: result_type,
            data: {
                keys: result_keys,
                values: result_values
            }
        }
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchSvButton: dispatch.bind(setResult)
    }
}

// pass selected properties from redux state tree to component
const ResultState = connect(
    mapStateToProps,
    mapDispatchToProps
)(ResultLayout)

// indicate which class can be exported, and instantiated via 'require'
export default ResultState
