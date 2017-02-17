/**
 * router.jsx: defines react-router tree.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Router, Route, browserHistory } from 'react-router';
import DataNewState from './import/redux/container/data-new-container.jsx';
import DataAppendState from './import/redux/container/data-append-container.jsx';
import ModelGenerateState from './import/redux/container/model-generate-container.jsx';
import ModelPredictState from './import/redux/container/model-predict-container.jsx';
import RegisterState from './import/redux/container/register-container.jsx';
import AnalysisLayoutState from './import/redux/container/analysis-layout-container.jsx';
import PageLayout from './import/layout/page-layout.jsx';
import LoginLayout from './import/layout/login-layout.jsx';
import RegisterLayout from './import/layout/register-layout.jsx';
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
                    <Route path='/session' component={AnalysisLayoutState}>
                        <Route
                            path='/session/data-new'
                            components={{
                                content: DataNewState,
                                session_type_value: 'data_new'
                            }}
                        />
                        <Route
                            path='/session/data-append'
                            components={{
                                content: DataAppendState,
                                session_type_value: 'data_append'
                            }}
                        />
                        <Route
                            path='/session/model-generate'
                            components={{
                                content: ModelGenerateState,
                                session_type_value: 'model_generate'
                            }}
                        />
                        <Route
                            path='/session/model-predict'
                            components={{
                                content: ModelPredictState,
                                session_type_value: 'model_predict'
                            }}
                        />
                    </Route>
                    <Route
                        path='/login'
                        components={{
                            content: LoginLayout,
                            sidebar: null,
                            css: 'main-full-span login-form',
                            layout: 'login'
                        }}
                    />
                    <Route
                        path='/logout'
                        components={{
                            content: LoginLayout,
                            sidebar: null,
                            css: 'main-full-span login-form',
                            layout: 'login'
                        }}
                    />
                    <Route
                        path='/register'
                        components={{
                            content: RegisterLayout,
                            sidebar: null,
                            css: 'main-full-span register-form',
                            layout: 'register'
                        }}
                    />
                </Route>
            </Router>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export { AppRouter, AnalysisLayout }
