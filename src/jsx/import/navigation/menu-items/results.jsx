/**
 * results.jsx: results link markup.
 *
 * @ReviewResultsLink, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import ajaxCaller from '../../general/ajax-caller.js';

class ReviewResultsLink extends Component {
    // initial 'state properties'
    constructor() {
        super();
        this.state = {
            ajax_done_result: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null,
        };
        this.renderContent = this.renderContent.bind(this);
    }
    // call back: return login button
    renderContent() {
        if (
            (
                this.state.ajax_done_result &&
                this.state.ajax_done_result.titles.length > 0
            ) ||
            (
                this.props &&
                this.props.page &&
                this.props.page.button &&
                this.props.page.button.review_results
            )
        ) {
            return (
                <NavLink
                    to='/session/results'
                    activeClassName='active'
                    className='menu-item'
                >
                    Review Results
                </NavLink>
            );
        }
        return null;
    }
    componentWillMount() {
        // local variables
        const ajaxArguments = {
            endpoint: '/retrieve-prediction-titles',
        };

        // asynchronous callback: ajax 'done' promise
        ajaxCaller(
            (asynchObject) => {
                // Append to DOM
                if (asynchObject && asynchObject.error) {
                    this.setState({ ajax_done_error: asynchObject.error });
                } else if (asynchObject) {
                    this.setState({ ajax_done_result: asynchObject });
                } else {
                    this.setState({ ajax_done_result: null });
                }
                // boolean to hide ajax spinner
                this.setState({ display_spinner: false });
            },
            // asynchronous callback: ajax 'fail' promise
            (asynchStatus, asynchError) => {
                if (asynchStatus) {
                    this.setState({ ajax_fail_status: asynchStatus });
                    console.log(`Error Status: ${asynchStatus}`);
                }
                if (asynchError) {
                    this.setState({ ajax_fail_error: asynchError });
                    console.log(`Error Thrown: ${asynchError}`);
                }
                // boolean to hide ajax spinner
                this.setState({ display_spinner: false });
            },
            // pass ajax arguments
            ajaxArguments,
        );
    }
    render() {
        const selectedContent = this.renderContent();
        return (selectedContent);
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default ReviewResultsLink;
