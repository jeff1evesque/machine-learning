/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import ReactDOM from 'react-dom';
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

        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu onChange={this.setClickType} />
                </div>

                <MainContent
                    renderNavBar={navbar}
                    componentType={this.state.component_name}
                    sessionType={this.state.display_name}
                />
            </div>
        );
    }
});

// render form
//
// @indexRoute, is accessible within child component as 'this.props.indexRoute'
//
ReactDOM.render(
    <AppRouter indexRoute={Page} />,
    document.querySelector('.container')
);
