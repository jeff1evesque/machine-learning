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
            content_type
        } = this.props;

      // default value: session value
        if (!content_type || !content_type.type) {
            var contentSelection = '--Select--';
        }
        else {
            var contentSelection = content_type.type;
        }

      // determine content
        if (content && content_type && content_type.type == 'result') {
            var display_content = content;
        }
        else if (content && content_type && !!content_type.type) {
            var display_content = <SupportVectorState
                sessionType={content}
                sessionTypeValue={contentSelection}
            />;
        }
        else {
            var display_content = this.props.children;
        }

        return(
            <div className='analysis-container'>
                {display_content}
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default AnalysisLayout
