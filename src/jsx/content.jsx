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
import AppRouter from './router.jsx';
import store from './import/redux/store.jsx';

// render application
//
// @indexRoute, is accessible within child component as 'this.props.indexRoute'
//
// Note: the 'Provider' component, makes redux data to be accessible to all
//       container components, without passing it explicitly.
//
ReactDOM.render(
    <Provider store={store}>
        <AppRouter />
    </Provider>,
    document.querySelector('.container')
);
