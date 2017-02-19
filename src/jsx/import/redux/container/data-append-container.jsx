/**
 * data-append-container.jsx: redux store for general page settings, associated
 *                            with the data-append session.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import DataAppend from '../../session-type/data-append.jsx';
import setSvButton from '../action/page-action.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
  // validate button
    if (
        state &&
        state.page &&
        state.page.submit_button &&
        !!state.page.submit_button.analysis
    ) {
        var display = state.page.submit_button.analysis;
    }
    else {
        var display = false;
    }

  // return redux to state
    return {
        page: {
            submit_button: {analysis: display}
        }
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchSvButton: dispatch.bind(setSvButton)
    }
}

// pass selected properties from redux state tree to component
const DataAppendState = connect(
    mapStateToProps,
    mapDispatchToProps
)(DataAppend)

// indicate which class can be exported, and instantiated via 'require'
export default DataAppendState
