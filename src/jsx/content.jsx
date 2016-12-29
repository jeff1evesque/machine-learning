/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import createStore from 'redux';
import Provider from 'react-redux';
import MainContent from './import/main.jsx';
import NavBar from './import/navigation/nav_bar.jsx';
import UserMenu from './import/navigation/user_menu.jsx';
import AppRouter from './router.jsx';

var Page = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            render_subpage: 'SupportVector',
            display_name: 'none',
        };
    },
  // update 'state properties': click event has not 'target'
    setClickType: function(event){
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
    componentDidMount: function() {
        if (
            this.props &&
            this.props.children &&
            this.props.children.props &&
            this.props.children.props.children &&
            this.props.children.props.children.props &&
            this.props.children.props.children.props.route &&
            this.props.children.props.children.props.route.component &&
            this.props.children.props.children.props.route.component.name
        ) {
            var property = this.props.children.props.children.props;
            var componentName = property.route.component.name;

            if (
                componentName == 'LoginLayout' ||
                componentName == 'RegisterLayout'
            ) {
                this.setState({component_name: componentName});
                this.setState({display_name: 'none'});
            }
        }
    },
  // display result
    render: function() {
      // local variables
        var navbar = this.renderNavBar();

        if (
            this.props &&
            this.props.children &&
            this.props.children.props &&
            this.props.children.props.children &&
            this.props.children.props.children.props
        ) {
            var property = this.props.children.props.children.props;
        }

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

        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu onChange={this.setClickType} />
                </div>

                <MainContent
                    renderNavBar={navbar}
                    componentType={componentName}
                    sessionType={displayName}
                />
            </div>
        );
    }
});

// redux store: contains entire state tree for the application
store = createStore();

// render form
//
// @indexRoute, is accessible within child component as 'this.props.indexRoute'
//
ReactDOM.render(
    <Provider store={store}>
        <AppRouter indexRoute={Page} />
    </Provider>,
    document.querySelector('.container')
);
