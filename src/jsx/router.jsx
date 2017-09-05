/**
 * router.jsx: defines react-router tree.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Router, Route, browserHistory } from 'react-router';
import DataNewState from './import/redux/container/data-new.jsx';
import DataAppendState from './import/redux/container/data-append.jsx';
import ModelGenerateState from './import/redux/container/model-generate.jsx';
import ModelPredictState from './import/redux/container/model-predict.jsx';
import CurrentResultState from './import/redux/container/current-result.jsx';
import ResultsState from './import/redux/container/results.jsx';
import RegisterState from './import/redux/container/register.jsx';
import AnalysisLayoutState from './import/redux/container/analysis-layout.jsx';
import PageLayout from './import/layout/page.jsx';
import LoginLayout from './import/layout/login.jsx';
import RegisterLayout from './import/layout/register.jsx';
import NavBar from './import/navigation/nav-bar.jsx';

var AppRouter = React.createClass({
  // display result
    render: function() {
        {/* return:

            @history, is required per 'react-router's ability to handle url:

                - [GitHub-URL]/issues/2727#issuecomment-258030214

        */}

      // render routers
        return(
            <Router history={browserHistory}>
                <Route path='/' component={PageLayout}>
                    <Route
                        path='/session'
                        components={{
                            content: AnalysisLayoutState,
                            sidebar: NavBar,
                            css: 'container analysis-container',
                            layout: 'analysis'
                        }}
                    >
                        <Route
                            path='/session/data-new'
                            components={{
                                content: DataNewState,
                                content_type: 'data_new'
                            }}
                        />
                        <Route
                            path='/session/data-append'
                            components={{
                                content: DataAppendState,
                                content_type: 'data_append'
                            }}
                        />
                        <Route
                            path='/session/model-generate'
                            components={{
                                content: ModelGenerateState,
                                content_type: 'model_generate'
                            }}
                        />
                        <Route
                            path='/session/model-predict'
                            components={{
                                content: ModelPredictState,
                                content_type: 'model_predict'
                            }}
                        />
                        <Route
                            path='/session/current-result'
                            components={{
                                content: CurrentResultState,
                                content_type: 'result'
                            }}
                        />
                        <Route
                            path='/session/results'
                            components={{
                                content: ResultsState,
                                content_type: 'result'
                            }}
                        />
                    </Route>
                    <Route
                        path='/login'
                        components={{
                            content: LoginLayout,
                            sidebar: null,
                            css: 'container login',
                            layout: 'login'
                        }}
                    />
                    <Route
                        path='/logout'
                        components={{
                            content: LoginLayout,
                            sidebar: null,
                            css: 'container login',
                            layout: 'login'
                        }}
                    />
                    <Route
                        path='/register'
                        components={{
                            content: RegisterLayout,
                            sidebar: null,
                            css: 'container register',
                            layout: 'register'
                        }}
                    />
                </Route>
            </Router>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default AppRouter
