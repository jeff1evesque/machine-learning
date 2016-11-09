/**
 * router.jsx: defines react-router tree.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Router, Route, browserHistory } from 'react-router'
import DataNew from './import/session-type/data_new.jsx';
import DataAppend from './import/session-type/data_append.jsx';
import ModelGenerate from './import/session-type/model_generate.jsx';
import ModelPredict from './import/session-type/model_predict.jsx';
import SupportVector from './import/content/support_vector.jsx';
import LoginForm from './import/content/login.jsx';
import RegisterForm from './import/content/register.jsx';

// constant: analysis layout
const AnalysisLayout = (props) => (
    <div className='analysis-container'>
        <SupportVector routerProp={props.children} />
    </div>
);

// constant: inner container
const InnerMain = (props) => (
    <div className='main-inner'>
        <AnalysisLayout />
    </div>
);

// constant: login layout
const LoginLayout = (props) => (
    <div className='main-full-span login-form'>
        <LoginForm routerProp={props.children} />
    </div>
);

// constant: register layout
const RegisterLayout = (props) => (
    <div className='main-full-span register-form'>
        <RegisterForm routerProp={props.children} />
    </div>
);

// application router
var AppRouter = React.createClass({
  // display result
    render: function() {
        {/* return:
            @this.props.indexRoute, defined from parent component.
            @this.props.subpage, defined from parent component.
            @history, is required per 'react-router's ability to handle url:

                - [GitHub-URL]/issues/2727#issuecomment-258030214
        */}

      // render routers
        return(
            <Router history={browserHistory}>
                <Route component={this.props.indexRoute}>
                    <Route path='/' component={InnerMain}>
                        <Route path='/session' component={AnalysisLayout}>
                            <Route
                                path='/session/data-new'
                                component={DataNew}
                            />
                            <Route
                                path='/session/data-append'
                                component={DataAppend}
                            />
                            <Route
                                path='/session/model-generate'
                                component={ModelGenerate}
                            />
                            <Route
                                path='/session/model-predict'
                                component={ModelPredict}
                            />
                        </Route>
                        <Route path='/login' component={LoginLayout} />
                        <Route path='/register' component={RegisterLayout} />
                    </Route>
                </Route>
            </Router>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default AppRouter
