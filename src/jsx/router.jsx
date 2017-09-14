/**
 * router.jsx: defines react-router tree.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Router, Route, Switch } from 'react-router-dom';
import createBrowserHistory from 'history/createBrowserHistory';
import RegisterState from './import/redux/container/register.jsx';
import PageLayout from './import/layout/page.jsx';
import LoginLayout from './import/layout/login.jsx';
import RegisterLayout from './import/layout/register.jsx';

const history = createBrowserHistory();
var AppRouter = React.createClass({
  // display result
    render: function() {
        {/* return:

            @history, is required per 'react-router's ability to handle url:

                - [GitHub-URL]/issues/2727#issuecomment-258030214

        */}

      // render routers
        return(
            <Router history={history}>
                <Switch>
                    <Route path='/' component={PageLayout} />
                    <Route
                        exact
                        path='/login'
                        components={{
                            content: LoginLayout,
                            sidebar: null,
                            css: 'container login',
                            layout: 'login'
                        }}
                    />
                    <Route
                        exact
                        path='/logout'
                        components={{
                            content: LoginLayout,
                            sidebar: null,
                            css: 'container login',
                            layout: 'login'
                        }}
                    />
                    <Route
                        exact
                        path='/register'
                        components={{
                            content: RegisterLayout,
                            sidebar: null,
                            css: 'container register',
                            layout: 'register'
                        }}
                    />
                </Switch>
            </Router>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default AppRouter
