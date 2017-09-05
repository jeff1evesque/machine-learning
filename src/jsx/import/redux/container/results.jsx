/**
 * results.jsx: redux store for obtaining list of all results.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import ResultsDisplay from '../../result/results.jsx';
import getCurrentResult from '../action/results.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    var resultType = null;
    var resultData = null;

    if (
        state &&
        state.data &&
        state.data.results &&
        !!state.data.results.status == 0 &&
        !!state.data.results.title &&
    ) {
        if (
            !!state.data.results.title[0][1] &&
            !!state.data.results.title[0][0]
        ) {
            const svm_date = state.data.results.title[0][1];
            const svr_date = state.data.results.title[1][1];
        }
        else if (
            !!state.data.results.title[1][1] &&
            !!state.data.results.title[1][0]
        ) {
            const svm_title = state.data.results.title[0][0];
            const svr_title = state.data.results.title[1][0];
        }
    }

  // return redux to state
    return {
        results: {
            type: resultType,
            data: resultData
        }
    }
}

// pass selected properties from redux state tree to component
const ResultsState = connect(
    mapStateToProps
)(ResultsDisplay)

// indicate which class can be exported, and instantiated via 'require'
export default ResultsState
