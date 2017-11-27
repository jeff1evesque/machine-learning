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
import {
    setSvButton,
    setGotoResultsButton,
    setLayout,
    setContentType,
    setSpinner
} from '../action/page.jsx';

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchSvButton: dispatch.bind(setSvButton),
        dispatchGotoResultsButton: dispatch.bind(setGotoResultsButton),
        dispatchContentType: dispatch.bind(setContentType),
        dispatchLayout: dispatch.bind(setLayout),
        dispatchSpinner: dispatch.bind(setSpinner)
    }
}

// pass selected properties from redux state tree to component
const ModelPredictState = connect(
    null,
    mapDispatchToProps
)(ModelPredict)

// indicate which class can be exported, and instantiated via 'require'
export default ModelPredictState
