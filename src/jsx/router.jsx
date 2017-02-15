/**
 * router.jsx: defines react-router tree.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Router, Route, browserHistory } from 'react-router';
import DataNew from './import/session-type/data-new.jsx';
import DataAppend from './import/session-type/data-append.jsx';
import ModelGenerate from './import/session-type/model-generate.jsx';
import ModelPredict from './import/session-type/model-predict.jsx';
import SupportVector from './import/content/support-vector.jsx';
import LoginState from './import/redux/container/login-container.jsx';
import RegisterState from './import/redux/container/register-container.jsx';
import PageLayout from './import/page-layout.jsx';
import NavBar from './import/navigation/nav-bar.jsx';

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
        if (!session_type_value || !session_type_value.key) {
            var session_type_value = '--Select--'});
        }

        return(
            <div className='analysis-container'>
                <SupportVector
                    sessionType={content}
                    sessionTypeValue={session_type_value}
                />
            </div>
        );
    }
});

var LoginLayout = React.createClass({
    render: function() {
        return(
            <div className='main-full-span login-form'>
                <LoginState />
            </div>
        );
    }
});

var RegisterLayout = React.createClass({
    render: function() {
        return(
            <div className='main-full-span register-form'>
                <RegisterState />
            </div>
        );
    }
});

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
                            content: AnalysisLayout,
                            sidebar: NavBar,
                            css: 'analysis-container',
                            layout: 'analysis'
                        }}
                    >
                        <Route
                            path='/session/data-new'
                            components={{
                                content: DataNew,
                                session_type_value: 'data_new'
                            }}
                        />
                        <Route
                            path='/session/data-append'
                            components={{
                                content: DataAppend,
                                session_type_value: 'data_append'
                            }}
                        />
                        <Route
                            path='/session/model-generate'
                            components={{
                                content: ModelGenerate,
                                session_type_value: 'model_generate'
                            }}
                        />
                        <Route
                            path='/session/model-predict'
                            components={{
                                content: ModelPredict,
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
export default AppRouter
