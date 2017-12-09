/**
 * model-generate.jsx: redux store for general page settings, associated with
 *                     the data-new session.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import ModelGenerate from '../../session-type/model-generate.jsx';
import {
    setSvButton,
    setLayout,
    setContentType,
    setSpinner
} from '../action/page.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    var penalty = 0;

    if (
        state &&
        state.page &&
        state.page.slider &&
        state.page.slider.penalty &&
        !!state.page.slider.penalty
    ) {
        var penalty = state.page.slider.penalty;
    }

  // return redux to state
    return {
        page: {
            slider: {
                penalty: penalty
            }
        }
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchSvButton: dispatch.bind(setSvButton),
        dispatchContentType: dispatch.bind(setContentType),
        dispatchLayout: dispatch.bind(setLayout),
        dispatchSpinner: dispatch.bind(setSpinner)
    }
}

// pass selected properties from redux state tree to component
const ModelGenerateState = connect(
    mapStateToProps,
    mapDispatchToProps
)(ModelGenerate)

// indicate which class can be exported, and instantiated via 'require'
export default ModelGenerateState
