/**
 * analysis.jsx: general analysis layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import { Route, Switch } from 'react-router-dom';
import DataNewState from '../redux/container/data-new.jsx';
import DataAppendState from '../redux/container/data-append.jsx';
import ModelGenerateState from '../redux/container/model-generate.jsx';
import ModelPredictState from '../redux/container/model-predict.jsx';
import SupportVectorState from '../redux/container/support-vector.jsx';
import CurrentResultState from '../redux/container/current-result.jsx';
import ResultsDisplay from '../result/results.jsx';

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
            <div>
                <Switch>
                    <Route
                        exact
                        path='/session/data-new'
                        components={{
                            content: DataNewState,
                            content_type: 'data_new'
                        }}
                    />
                    <Route
                        exact
                        path='/session/data-append'
                        components={{
                            content: DataAppendState,
                            content_type: 'data_append'
                        }}
                    />
                    <Route
                        exact
                        path='/session/model-generate'
                        components={{
                            content: ModelGenerateState,
                            content_type: 'model_generate'
                        }}
                    />
                    <Route
                        exact
                        path='/session/model-predict'
                        components={{
                        content: ModelPredictState,
                            content_type: 'model_predict'
                        }}
                    />
                    <Route
                        exact
                        path='/session/current-result'
                        components={{
                            content: CurrentResultState,
                            content_type: 'result'
                        }}
                    />
                    <Route
                        exact
                        path='/session/results'
                        components={{
                            content: ResultsDisplay,
                            content_type: 'result'
                        }}
                    />
                <div className='analysis-container'>
                    {display_content}
                </div>
                </Switch>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default AnalysisLayout
