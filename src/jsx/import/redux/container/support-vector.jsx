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
import { setGotoResultsButton, setSvButton } from '../action/page.jsx';
import setCurrentResult from '../action/current-result.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    var resultsBtn = false;
    var submitAnalysisBtn = false;

    if (
        state &&
        state.page &&
        state.page.button
    ) {
        const button = state.page.button;
        var resultsBtn = !!button.goto_results ? button.goto_results : null;
        var submitBtn = !!button.submit_analysis ? button.submit_analysis : null;
    }

  // return redux to state
    return {
        page: {
            button: {
                goto_results: resultsBtn,
                submit_analysis: submitBtn
            }
        }
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchSvButton: dispatch.bind(setSvButton),
        dispatchResults: dispatch.bind(setCurrentResult),
        dispatchGotoResultsButton: dispatch.bind(setGotoResultsButton)
    }
}

// pass selected properties from redux state tree to component
const SupportVectorState = connect(
    mapStateToProps,
    mapDispatchToProps
)(SupportVector)

// indicate which class can be exported, and instantiated via 'require'
export default SupportVectorState
