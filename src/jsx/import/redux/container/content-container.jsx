/**
 * content-container.jsx: redux store for general page settings.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import Page from '../../../content.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    return {
        page: {
            layout: state.page.layout
        }
    }
}

// pass selected properties from redux state tree to component
const PageState = connect(
    mapStateToProps,
    null
)(Page)

// indicate which class can be exported, and instantiated via 'require'
export default PageState
