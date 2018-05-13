/**
 * result-route.jsx: result routes.
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
import CurrentResultState from '../redux/container/current-result.jsx';
import ResultsDisplayState from '../redux/container/results.jsx';

class ResultRoute extends Component {
    render() {
        return (
            <div>
                <Route
                    component={CurrentResultState}
                    exact
                    path='/session/current-result'
                />
                <Route
                    component={ResultsDisplayState}
                    exact
                    path='/session/results'
                />
            </div>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default ResultRoute;
