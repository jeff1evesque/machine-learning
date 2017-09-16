/**
 * login.jsx: redux store for general page settings.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import PageLayout from '../../layout/page.jsx';
import { setLayout } from '../action/page.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
  // return redux to state
    return {
        layout: {
            type: state.layout,
            css: state.css
        }
    }
}

// wraps each function of the object to be dispatch callable
const mapDispatchToProps = (dispatch) => {
    return {
        dispatchLayout: dispatch.bind(setLayout)
    }
}

// pass selected properties from redux state tree to component
const PageLayoutState = connect(
    mapStateToProps,
    mapDispatchToProps
)(PageLayout)

// indicate which class can be exported, and instantiated via 'require'
export default PageLayoutState
