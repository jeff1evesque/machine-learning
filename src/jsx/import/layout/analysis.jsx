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
import ResultsDisplayState from '../redux/container/results.jsx';

var AnalysisLayout = React.createClass({
    getSessionType: function(type) {
        return {
            data_new: DataNewState,
            data_append: DataAppendState,
            model_generate: ModelGenerateState,
            model_predict: ModelPredictState
        }[type] || 'span';
    },
    render: function() {
      // determine content
        var sessionType = this.props.page.content_type;
        var content = this.getSessionType(sessionType);

        if (sessionType == 'result') {
            var display_content = content;
        }
        else if (!!sessionType) {
            var display_content = <SupportVectorState
                sessionType={content}
                sessionTypeValue={sessionType}
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
                        component={DataNewState}
                    />
                    <Route
                        exact
                        path='/session/data-append'
                        component={DataAppendState}
                    />
                    <Route
                        exact
                        path='/session/model-generate'
                        component={ModelGenerateState}
                    />
                    <Route
                        exact
                        path='/session/model-predict'
                        component={ModelPredictState}
                    />
                    <Route
                        exact
                        path='/session/current-result'
                        component={CurrentResultState}
                    />
                    <Route
                        exact
                        path='/session/results'
                        component={ResultsDisplayState}
                    />
                </Switch>
                <div className='analysis-container'>
                    {display_content}
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default AnalysisLayout
