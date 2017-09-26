/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { Router, Switch } from 'react-router-dom';
import PageLayoutState from './import/redux/container/page.jsx';
import createHistory from 'history/createBrowserHistory';
import store from './import/redux/store.jsx';

// local variables
const history = createHistory();

// render application
//
// @Provider, allows a common redux state tree, be accessible to all
//     connected react components, when integrated with a common 'store'. This
//     elimates the hassle associated with passing properites between parent,
//     and children react components.
//
ReactDOM.render(
    <Provider store={store}>
        <Router history={history}>
            <Switch>
                <PageLayoutState />
            </Switch>
        </Router>
    </Provider>,
    document.querySelector('.container')
);
