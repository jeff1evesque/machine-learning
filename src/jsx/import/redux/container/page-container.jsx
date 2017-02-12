/**
 * page-container.jsx: redux store for general page settings.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import PageLayout from '../../page-layout.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
  // validate layout
    if (state && state.page && !!state.page.layout) {
        var layout = state.page.layout
    }
    else {
        var layout = 'default'
    }

    return {
        page: {
            layout: layout
        }
    }
}

// pass selected properties from redux state tree to component
const PageState = connect(
    mapStateToProps,
    null
)(PageLayout)

// indicate which class can be exported, and instantiated via 'require'
export default PageState
