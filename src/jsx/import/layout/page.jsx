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
import Spinner from '../general/spinner.jsx';
import HomePageState from '../redux/container/home-page.jsx';
import UserMenuState from '../redux/container/user-menu.jsx';
import HeaderMenuState from '../redux/container/header-menu.jsx';
import AnalysisLayoutState from '../redux/container/analysis-layout.jsx';

var PageLayout = React.createClass({
  // callback: used to return spinner
    getSpinner: function() {
        if (this.props && this.props.effects && this.props.effects.spinner) {
            return <Spinner />;
        } else {
            return null;
        }
    },
    render: function() {
      // local variables
        var spinner = this.getSpinner();

      // validate username
        if (
            this.props &&
            this.props.user &&
            !!this.props.user.name &&
            this.props.user.name != 'anonymous'
        ) {
            var mainMenu = <UserMenuState />;
        }
        else {
            var mainMenu = <div className='container'><HeaderMenuState /></div>;
        }

        return(
            <div>
                <div className='menu-container'>
                    {mainMenu}
                </div>
                <div className='main'>
                    <Route exact path='/login' component={LoginLayout} />
                    <Route exact path='/logout' component={LoginLayout} />
                    <Route exact path='/register' component={RegisterLayout} />
                    <Route path='/session' component={AnalysisLayoutState} />
                </div>
                <Route exact path='/' component={HomePageState} />
                {spinner}
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
