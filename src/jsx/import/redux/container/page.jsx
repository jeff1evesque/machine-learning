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

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
  // validate username
    if (state && state.user && !!state.user.name) {
        var username = state.user.name
    } else {
        var username = 'anonymous'
    }

  // fetch spinner
    if (
        state &&
        state.page &&
        state.page.effects &&
        state.page.effects.spinner
    ) {
        var spinnerBool = true;
    } else {
        var spinnerBool = false;
    }

  // return redux to state
    return {
        user: {
            name: username
        },
        effects: {
            spinner: spinnerBool
        }
    }
}

// pass selected properties from redux state tree to component
const PageLayoutState = connect(
    mapStateToProps,
    null
)(PageLayout)

// indicate which class can be exported, and instantiated via 'require'
export default PageLayoutState
