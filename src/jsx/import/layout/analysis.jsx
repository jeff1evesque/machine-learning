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
    getSessionType: function(type) {
        return {
            data_new: DataNewState,
            data_append: DataAppendState,
            model_generate: ModelGenerateState,
            model_predict: ModelPredictState
        }[type] || 'span';
    },
    render: function() {
      // destructure react-router
        var css = this.props.page.css;
        var contentType = this.props.page.content_type;
        var content = getSessionType(contentType);

      // default value: session value
        if (!content_type || !content_type.type) {
            var contentSelection = '--Select--';
        }
        else {
            var contentSelection = content_type.type;
        }

      // determine content
        if (contentType == 'result') {
            var display_content = content;
        }
        else if (!!contentType) {
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
                        render = {(props) =>
                    {
                        return(
                            <div>
                              // update redux store
                                const action = setContentType('data_new');
                                this.props.dispatchContentType(action);

                              // render component
                                <DataNewState />
                            </div>
                        )
                    }} />
                    <Route
                        exact
                        path='/session/data-append'
                        render = {(props) =>
                    {
                        return(
                            <div>
                              // update redux store
                                const action = setContentType('data_append');
                                this.props.dispatchContentType(action);

                              // render component
                                <DataAppendState />
                            </div>
                        )
                    }} />
                    <Route
                        exact
                        path='/session/model-generate'
                        render = {(props) =>
                    {
                        return(
                            <div>
                              // update redux store
                                const action = setContentType('model_generate');
                                this.props.dispatchContentType(action);

                              // render component
                                <ModelGenerateState />
                            </div>
                        )
                    }} />
                    <Route
                        exact
                        path='/session/model-predict'
                        render = {(props) =>
                    {
                        return(
                            <div>
                              // update redux store
                                const action = setContentType('model_predict');
                                this.props.dispatchContentType(action);

                              // render component
                                <ModelPredictState />
                            </div>
                        )
                    }} />
                    <Route
                        exact
                        path='/session/current-result'
                        render = {(props) =>
                    {
                        return(
                            <div>
                              // update redux store
                                const action = setContentType('result');
                                this.props.dispatchContentType(action);

                              // render component
                                <CurrentResultState />
                            </div>
                        )
                    }} />
                    <Route
                        exact
                        path='/session/results'
                        render = {(props) =>
                    {
                        return(
                            <div>
                              // update redux store
                                const action = setContentType('result');
                                this.props.dispatchLogin(action);

                              // render component
                                <ResultsDisplay />
                            </div>
                        )
                    }} />
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
