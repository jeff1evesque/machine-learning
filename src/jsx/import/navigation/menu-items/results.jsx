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

import React from 'react';
import { NavLink } from 'react-router-dom';
import ajaxCaller from '../../general/ajax-caller.js';

var ReviewResultsLink = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            ajax_done_result: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null
        };
    },
  // call back: return login button
    renderContent: function() {
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
        } else {
            return null;
        }
    },
    componentWillMount: function() {
      // local variables
        var ajaxArguments = {
            'endpoint': '/retrieve-prediction-titles'
        };

      // asynchronous callback: ajax 'done' promise
        ajaxCaller(function (asynchObject) {
          // Append to DOM
            if (asynchObject && asynchObject.error) {
                this.setState({ajax_done_error: asynchObject.error});
            } else if (asynchObject) {
                this.setState({ajax_done_result: asynchObject});
            } else {
                this.setState({ajax_done_result: null});
            }
        // boolean to hide ajax spinner
            this.setState({display_spinner: false});
        }.bind(this),
      // asynchronous callback: ajax 'fail' promise
        function (asynchStatus, asynchError) {
            if (asynchStatus) {
                this.setState({ajax_fail_status: asynchStatus});
                console.log('Error Status: ' + asynchStatus);
            }
            if (asynchError) {
                this.setState({ajax_fail_error: asynchError});
                console.log('Error Thrown: ' + asynchError);
            }
        // boolean to hide ajax spinner
            this.setState({display_spinner: false});
        }.bind(this),
      // pass ajax arguments
        ajaxArguments);
    },
    render: function(){
        var selectedContent = this.renderContent();
        return(selectedContent);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ReviewResultsLink
