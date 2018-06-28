/**
 * main-route.jsx: upper level routes.
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
import LoginLayout from '../layout/login.jsx';
import RegisterLayout from '../layout/register.jsx';
import HomePageState from '../redux/container/home-page.jsx';
import AnalysisLayoutState from '../redux/container/analysis-layout.jsx';

class MainRoute extends Component {
    render() {
        return (
            <div className='row'>
                <Route
                    component={HomePageState}
                    exact
                    path='/'
                />
                <Route
                    component={LoginLayout}
                    exact
                    path='/login'
                />
                <Route
                    component={LoginLayout}
                    exact
                    path='/logout'
                />
                <Route
                    component={RegisterLayout}
                    exact
                    path='/register'
                />
                <Route
                    component={AnalysisLayoutState}
                    path='/session'
                />
            </div>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default MainRoute;
