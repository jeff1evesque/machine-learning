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
import MainContent from './import/main.jsx';
import NavBar from './import/navigation/nav-bar.jsx';
import UserMenu from './import/navigation/user-menu.jsx';
import AppRouter from './router.jsx';
import store from './import/redux/store.jsx';
import HomePage from './import/content/home-page.jsx';

var Page = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            display_name: 'none',
        };
    },
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
            var SelectedContent = <MainContent renderNavBar={navbar} />;
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

// render form
//
// @indexRoute, is accessible within child component as 'this.props.indexRoute'
//
// Note: the 'Provider' component, makes redux data to be accessible to all
//       container components, without passing it explicitly.
//
ReactDOM.render(
    <Provider store={store}>
        <AppRouter indexRoute={Page} />
    </Provider>,
    document.querySelector('.container')
);
