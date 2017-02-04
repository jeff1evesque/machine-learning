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
            render_subpage: 'SupportVector',
            display_name: 'none',
        };
    },
  // update 'state properties': click event has not 'target'
    setClickType: function(event) {
        if (event.home) {
            this.setState({render_subpage: 'SupportVector'});
        }
        else if (event.login) {
            this.setState({render_subpage: 'LoginForm'});
        }
        else if (event.register) {
            this.setState({render_subpage: 'RegisterForm'});
        }
    },
  // call back: return side navigation
    renderNavBar: function() {
        if (
            this.state.render_subpage == 'LoginForm' ||
            this.state.render_subpage == 'RegisterForm'
        ) {
            return false;
        }
        else {
            return true;
        }
    },
  // main content or homepage
    renderContent: function() {

        if (
            this.props &&
            this.props.children &&
            this.props.children.props
        ) {
            var navbar = this.renderNavBar();
            var property = this.props.children.props;

          // page assignment: login, registration
            if (
                property &&
                property.route &&
                property.route.component &&
                property.route.component.name
            ) {
                var displayName = this.state.display_name;
                var componentName = property.route.component.name;

              // session assignment: analysis
                if (
                    property &&
                    property.children &&
                    property.children.props &&
                    property.children.props.route &&
                    property.children.props.route.component &&
                    property.children.props.route.component.displayName
                ) {
                    var route = property.children.props.route;
                    var displayName = route.component.displayName;
                    var componentName = property.route.component.name;
                }
            }
            else {
                var displayName = this.state.display_name;
                var componentName = this.state.component_name;
            }

            var SelectedContent = <MainContent
                                      renderNavBar={navbar}
                                      componentType={componentName}
                                      sessionType={displayName}
                                  />;
        }
        else {
            var SelectedContent = <HomePage />;
        }

        return SelectedContent;
    },
  // display result
    render: function() {
        var SelectedContent = this.renderContent();
        var componentName = 'Home';

      // page assignment: login, registration
        if (
            this.props &&
            this.props.children &&
            this.props.children.props
        ) {
            var property = this.props.children.props;

            if (
                property &&
                property.route &&
                property.route.component &&
                property.route.component.name
            ) {
                var componentName = property.route.component.name;
            }
        }

        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu
                        onChange={this.setClickType}
                        componentType={componentName}
                    />
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
