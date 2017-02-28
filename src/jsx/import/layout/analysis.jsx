/**
 * analysis.jsx: general analysis layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import SupportVectorState from '../redux/container/support-vector.jsx';
import ResultState from '../redux/container/results.jsx';

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
            content &&
            !!session_type_value &&
            session_type_value != '--Select--'
        ) {
            var content = <SupportVectorState
                              sessionType={content}
                              sessionTypeValue={session_type_value}
                          />;
        }
        else {
            var content = <ResultState />;
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
