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
import setContentType from '../action/page.jsx';
import AnalysisLayout from '../../layout/analysis.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    var displayGotoResults = false;

    if (
        state &&
        state.page &&
        state.page.button &&
        !!state.page.button.goto_results
    ) {
            var displayGotoResults = state.page.button.goto_results;
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
                goto_results: displayGotoResults
            }
            css: css,
            content_type: contentType
        }
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchContentType: dispatch.bind(setContentType)
    }
}

// pass selected properties from redux state tree to component
const AnalysisLayoutState = connect(
    mapStateToProps,
    mapDispatchToProps
)(AnalysisLayout)

// indicate which class can be exported, and instantiated via 'require'
export default AnalysisLayoutState
