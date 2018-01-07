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
import { breakpoints } from '../general/breakpoints.js';
import PropTypes from 'prop-types';

class PageLayout extends Component {
    // prob validation: static method, similar to class A {}; A.b = {};
    static propTypes = {
        effects: PropTypes.shape({
            spinner: PropTypes.bool.isRequired,
        }),
        user: PropTypes.shape({
            name: PropTypes.string.isRequired,
        }),
    }

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
            var mainMenu = <div><HeaderMenuState /></div>;
            var authStatus = 'anonymous';
        }

        return (
            <div className={`${bpoint}-viewport container-fluid`}>
                <div className={authStatus}>
                    <div className='menu-container'>
                        {mainMenu}
                    </div>
                    <div className='content'>
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
                    {spinner}
                </div>
            </div>
        );
    }
    render() {
        return (
            <BreakpointRender
                breakpoints={breakpoints}
                type='viewport'
            >
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
