/**
 * page.jsx: general page layout.
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
import { Route } from 'react-router-dom';
import LoginLayout from './login.jsx';
import RegisterLayout from './register.jsx';
import HomePageState from '../redux/container/home-page.jsx';
import UserMenuState from '../redux/container/user-menu.jsx';
import AnalysisLayoutState from '../redux/container/analysis-layout.jsx';

var PageLayout = React.createClass({
    render: function() {
      // default value: css classnames
        if (!!this.props && !!this.props.layout && !!this.props.layout.css) {
            var css = this.props.layout.css;
        } else {
            var css = 'container default';
        }

        return(
            <div>
            <div className={css}>
                <div className='menu-container'>
                    <UserMenuState />
                </div>
                <div className='main'>
                    <Route exact path='/login' component={LoginLayout} />
                    <Route exact path='/logout' component={LoginLayout} />
                    <Route exact path='/register' component={RegisterLayout} />
                    <Route path='/session' component={AnalysisLayoutState} />
                </div>
            </div>
            <Route exact path='/' component={HomePageState} />
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
