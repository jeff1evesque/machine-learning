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
            status: null
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
                const results = asynchObject;

                // enumerate and store response
                this.setState(Object.assign({}, results))
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
        const status = this.state.status;
        const titles = this.state.titles;

      // polyfill 'entries'
        if (!Object.entries) {
            entries.shim();
        }

      // generate result
        if (status == 0 && !!titles) {
            const resultList = <ul className='result-list'>{
                titles.map((title) => {
                    return <Link to={'/session/result?nid=' + titles[0]}>
                        <li key={'title-' + titles[0]}>
                            {titles[0]}: {titles[1]}
                        </li>
                    </Link>
                });
            }
        }
        else {
            const resultList = <div className='result-list'>
                Sorry, no results available!
            </div>;
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
