/**
 * session-route.jsx: main application sessions.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { Route } from 'react-router-dom';
import DataNewState from '../redux/container/data-new.jsx';
import DataAppendState from '../redux/container/data-append.jsx';
import ModelGenerateState from '../redux/container/model-generate.jsx';
import ModelPredictState from '../redux/container/model-predict.jsx';

class SessionRoute extends Component {
    render() {
        return (
            <div>
                <Route
                    component={DataNewState}
                    exact
                    path='/session/data-new'
                />
                <Route
                    component={DataAppendState}
                    exact
                    path='/session/data-append'
                />
                <Route
                    component={ModelGenerateState}
                    exact
                    path='/session/model-generate'
                />
                <Route
                    component={ModelPredictState}
                    exact
                    path='/session/model-predict'
                />
            </div>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default SessionRoute;
