/**
 * analysis-layout.jsx: redux store for general page settings.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import AnalysisLayout from '../../layout/analysis.jsx';
import { setLayout, setGotoResultsButton, setSvButton } from '../action/page.jsx';
import setCurrentResult from '../action/current-result.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    var contentType = false;
    var gotoResultsBtn = false;
    var submitBtn = false;

    if (
        state &&
        state.page &&
        state.page.button
    ) {
        const button = state.page.button;
        var submitBtn = !!button.submit_analysis ? button.submit_analysis : null;
        var gotoResultsBtn = !!button.goto_results ? button.goto_results : null;
    }

    if (
        state &&
        state.page &&
        !!state.page.content_type
    ) {
        var contentType = state.page.content_type;
    }

  // return redux to state
    return {
        page: {
            button: {
                goto_results: gotoResultsBtn,
                submit_analysis: submitBtn
            },
            content_type: contentType
        }
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchLayout: dispatch.bind(setLayout),
        dispatchSvButton: dispatch.bind(setSvButton),
        dispatchCurrentResult: dispatch.bind(setCurrentResult),
        dispatchGotoResultsButton: dispatch.bind(setGotoResultsButton)
    }
}

// pass selected properties from redux state tree to component
const AnalysisLayoutState = connect(
    mapStateToProps,
    mapDispatchToProps
)(AnalysisLayout)

// indicate which class can be exported, and instantiated via 'require'
export default AnalysisLayoutState
