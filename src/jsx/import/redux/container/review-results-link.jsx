/**
 * review-results-link.jsx: redux store 'review results' link state.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import { connect } from 'react-redux';
import ReviewResultsLink from '../../navigation/menu-items/results.jsx';

// transforms redux state tree to react properties
const mapStateToProps = (state) => {
    if (
        state &&
        state.page &&
        state.page.button
    ) {
        const button = state.page.button;
        var status = !!button.review_results ? button.review_results : false;
    }

  // return redux to state
    return {
        page {
            button: {
                review_results: status
            }
        }
    }
}

// pass selected properties from redux state tree to component
const LoginLinkState = connect(
    mapStateToProps,
    null
)(ReviewResultsLink)

// indicate which class can be exported, and instantiated via 'require'
export default ReviewResultsLink
