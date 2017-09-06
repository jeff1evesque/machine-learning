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
            data: null,
        };
    },
  // send form data to serverside on form submission
    handleSubmit: function(event) {
      // prevent page reload
        event.preventDefault();

      // local variables
        const ajaxEndpoint = '/retrieve-prediction-titles';

      // ajax process
        var ajaxArguments = {
            'endpoint': ajaxEndpoint,
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
  // define properties after update
    componentDidUpdate: function() {
        if (
            this.props &&
            this.props.results &&
            !!this.props.results.data &&
            this.state.data != JSON.stringify(this.props.data)
        ) {
            this.setState({
                nid: this.props.results.nid,
                data: JSON.stringify(this.props.results.data)
            });
        }
    },
    render: function(){
      // local variables
        var nid = null;
        var prediction = null;

        if (
            this.props &&
            this.props.results &&
            !!this.props.results.nid &&
            !!this.props.results.data
        ) {
            var nid = this.props.results.nid;
            var prediction = JSON.parse(this.props.results.data);
        }

      // polyfill 'entries'
        if (!Object.entries) {
            entries.shim();
        }

      // generate result
        if (
            nid &&
            prediction &&
            this.props &&
            this.props.results &&
            this.props.results.data &&
            Object.keys(prediction).length > 0
        ) {
            var resultList = <ul className='result-list'>{
                Object.entries(prediction).map(([item_key, value]) =>
                    <Link to={'/session/result/' + nid}>
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
