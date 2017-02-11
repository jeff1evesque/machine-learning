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
import MainContent from './main-content.jsx';
import NavBar from './navigation/nav-bar.jsx';
import UserMenu from './navigation/user-menu.jsx';
import HomePage from './content/home-page.jsx';

var PageLayout = React.createClass({
  // call back: return side navigation
    renderNavBar: function() {
        if (
            this.state.props.page.layout == 'login' ||
            this.state.props.page.layout == 'register'
        ) {
            return false;
        }
        else {
            return true;
        }
    },
  // main content or homepage
    renderContent: function() {
      // local variables
        var navbar = this.renderNavBar();

        if (
            this.state.props.page.layout == 'login' ||
            this.state.props.page.layout == 'register' ||
            this.state.props.page.layout == 'support-vector'
        ) {
            var SelectedContent = <MainContent
                                      renderNavBar={navbar}
                                      layout={this.state.props.layout}
                                  />;
        }
        else {
            var SelectedContent = <HomePage />;
        }

        return SelectedContent;
    },
  // display result
    render: function() {
      // local variables
        var SelectedContent = this.renderContent();

        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu />
                </div>

                {SelectedContent}
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default Layout
