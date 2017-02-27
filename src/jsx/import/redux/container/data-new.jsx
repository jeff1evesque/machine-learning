/**
 * data-new.jsx: redux store for general page settings, associated with the
 *               data-new session.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import DataNew from '../../session-type/data-new.jsx';
import { setSvButton } from '../action/page.jsx';

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchSvButton: dispatch.bind(setSvButton)
    }
}

// pass selected properties from redux state tree to component
const DataNewState = connect(
    null,
    mapDispatchToProps
)(DataNew)

// indicate which class can be exported, and instantiated via 'require'
export default DataNewState
