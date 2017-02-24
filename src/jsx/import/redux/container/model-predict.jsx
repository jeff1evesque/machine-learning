/**
 * model-predict.jsx: redux store for general page settings, associated with
 *                    the data-new session.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import ModelPredict from '../../session-type/model-predict.jsx';
import { setSvButton } from '../action/page.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    var displaySubmitAnalysis = false;
    var displayGotoResults = false;

    if (
        state &&
        state.page &&
        state.page.button
    ) {
        if  (!!state.page.button.submit_analysis) {
            var displaySubmitAnalysis = state.page.button.submit_analysis;
        }
        if (!!state.page.button.goto_results) {
            var displaySupportVectorResults = state.page.button.goto_results;
        }
    }

  // return redux to state
    return {
        page: {
            button: {
                submit_analysis: displaySubmitAnalysis,
                goto_results: displayGotoResults
            }
        }
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchSvButton: dispatch.bind(setSvButton),
        dispatchGotoResultsButton: dispatch.bind(setGotoResultsButton)
    }
}

// pass selected properties from redux state tree to component
const ModelPredictState = connect(
    mapStateToProps,
    mapDispatchToProps
)(ModelPredict)

// indicate which class can be exported, and instantiated via 'require'
export default ModelPredictState
