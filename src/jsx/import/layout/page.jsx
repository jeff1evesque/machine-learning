/**
 * page.jsx: general page layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React, { Component } from 'react';
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
import { BreakpointRender } from 'rearm/lib/Breakpoint';
import breakpoints from '../general/breakpoints.js';

class PageLayout extends Component {
    // callback: used to return spinner
    getSpinner() {
        if (this.props && this.props.effects && this.props.effects.spinner) {
            return <Spinner />;
        }
        return null;
    }
    renderContent(bpoint) {
        // local variables
        const spinner = this.getSpinner();

        // validate username
        if (
            this.props &&
            this.props.user &&
            !!this.props.user.name &&
            this.props.user.name != 'anonymous'
        ) {
            var mainMenu = <UserMenuState />;
            var authStatus = 'authenticated';
        } else {
            var mainMenu = <div className='container'><HeaderMenuState /></div>;
            var authStatus = 'anonymous';
        }

        return (
            <div className={`${bpoint}-viewport`}>
                <div className={authStatus}>
                    <div className='menu-container'>
                        {mainMenu}
                    </div>
                    <div className='container-fluid'>
                        <Route exact path='/' component={HomePageState} />
                        <Route exact path='/login' component={LoginLayout} />
                        <Route exact path='/logout' component={LoginLayout} />
                        <Route exact path='/register' component={RegisterLayout} />
                        <Route path='/session' component={AnalysisLayoutState} />
                    </div>
                    {spinner}
                </div>
            </div>
        );
    }
    render() {
        return (
            <BreakpointRender breakpoints={breakpoints} type='viewport'>
                {bp => (
                    bp.isGt('medium')
                        ? this.renderContent('large')
                        : (
                            bp.isGt('small') && bp.isLte('medium')
                                ? this.renderContent('medium')
                                : this.renderContent('small')
                        )
                )}
            </BreakpointRender>
        );
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout;
