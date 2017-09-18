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
import CurrentResultDisplay from '../../result/current-result.jsx';
import setCurrentResult from '../action/current-result.jsx';
import { setContentType } from '../action/page.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    var resultType = 'default';
    var resultData = null;

    if (
        state &&
        state.data &&
        state.data.results &&
        !!state.data.results.type &&
        !!state.data.results.data
    ) {
        var resultType = state.data.results.type;
        var resultData = state.data.results.data;
    }

  // return redux to state
    return {
        results: {
            type: resultType,
            data: resultData
        }
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchSvButton: dispatch.bind(setCurrentResult),
        dispatchContentType: dispatch.bind(setContentType)
    }
}

// pass selected properties from redux state tree to component
const CurrentResultState = connect(
    mapStateToProps,
    mapDispatchToProps
)(CurrentResultDisplay)

// indicate which class can be exported, and instantiated via 'require'
export default CurrentResultState
