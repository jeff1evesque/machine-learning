/**
 * router.jsx: defines react-router tree.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Router, Route, Switch } from 'react-router-dom';
import createBrowserHistory from 'history/createBrowserHistory';
import PageLayoutState from './import/redux/container/page.jsx';
import HomePage from './import/content/home-page.jsx';

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
                    <Route path='/' component={HomePage} />
                    <PageLayoutState />
                </Switch>
            </Router>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default AppRouter
