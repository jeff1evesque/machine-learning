/**
 * analysis.jsx: general analysis layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import SupportVectorState from '../redux/container/support-vector.jsx';

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

        return(
            <div className='analysis-container'>
                <SupportVectorState
                    sessionType={content}
                    sessionTypeValue={session_type_value}
                    submitSvButton={this.props.page.button.submit_analysis}
                />
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default AnalysisLayout
