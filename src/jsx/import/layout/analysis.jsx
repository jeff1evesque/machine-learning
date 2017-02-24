/**
 * analysis.jsx: general analysis layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import SupportVectorState from '../redux/container/support-vector.jsx';
import ResultDisplay from '../result/result-display.jsx';

var AnalysisLayout = React.createClass({
    render: function() {
      // destructure react-router
        var {
            content,
            session_type_value
        } = this.props;

      // default value: content
        if (!content) {
            var content = null;
        }

      // default value: session value
        if (!session_type_value || !session_type_value.type) {
            var session_type_value = '--Select--';
        }

      // determine content
        if (
            this.props.page &&
            this.props.page.button &&
            !!this.props.page.button.goto_results
        ) {
            var content = <ResultDisplay />
        }
        else {
            const submit_analysis = this.props.page.button.submit_analysis;
            var content = <SupportVectorState
                              sessionType={content}
                              sessionTypeValue={session_type_value}
                              submitSvButton={submit_analysis}
                          />
        }

        return(
            <div className='analysis-container'>
                {content}
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default AnalysisLayout
