/**
 * results.jsx: list all prediction result, with link to corresponding
 *              prediction result item.
 *
 * @CurrentResultDisplay, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import 'core-js/modules/es7.object.entries';
import Spinner from '../general/spinner.jsx';
import ajaxCaller from '../general/ajax-caller.js';

var ResultsDisplay = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            nid: null,
            titles: null,
        };
    },
  // call back: get all titles, and nid from server side
    componentDidMount: function() {
      // ajax arguments
        const ajaxEndpoint = '/retrieve-prediction-titles';
        const ajaxArguments = {
            'endpoint': ajaxEndpoint,
            'data': null
        };

      // boolean to show ajax spinner
        this.setState({display_spinner: true});

      // asynchronous callback: ajax 'done' promise
        ajaxCaller(function (asynchObject) {
        // Append to DOM
            if (asynchObject && asynchObject.error) {
                this.setState({ajax_done_error: asynchObject.error});
            } else if (asynchObject) {
                this.setState({ajax_done_result: asynchObject});
            }
            else {
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
      // local variables
        const results = this.state.ajax_done_result.titles;

      // polyfill 'entries'
        if (!Object.entries) {
            entries.shim();
        }

      // generate result
        if (results) {
            var resultList = <ul className='result-list'>{
                Object.entries(results).map(([item_key, value]) =>
                    <Link to={'/session/result?nid=' + item_key}>
                        <li key={item_key}>{item_key}: {value}</li>
                    </Link>
                )
            }</ul>;
        }
        else {
            var resultList = <div className='result-list'>Sorry, no results available!</div>;
        }

      // display result
        return(
            <div className='result-container'>
                <div>{resultList}</div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ResultsDisplay
