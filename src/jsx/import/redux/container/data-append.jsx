/**
 * data-append.jsx: redux store for general page settings, associated with the
 *                  data-append session.
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
import { setSvButton, setLayout, setContentType, setContentType } from '../action/page.jsx';

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchSvButton: dispatch.bind(setSvButton),
        dispatchContentType: dispatch.bind(setContentType),
        dispatchLayout: dispatch.bind(setLayout)
    }
}

// pass selected properties from redux state tree to component
const DataAppendState = connect(
    null,
    mapDispatchToProps
)(DataAppend)

// indicate which class can be exported, and instantiated via 'require'
export default DataAppendState
