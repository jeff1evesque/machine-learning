/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import NavBar from './import/navigation/nav_bar.jsx';
import SupportVector from './import/content/support_vector.jsx';
import LoginForm from './import/content/login.jsx';
import AppRouter from './router.jsx';

var Page = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            render_login: false,
            render_registration: false,
            render_subpage: 'SupportVector',
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
  // call back: generate main content
    getContent: function() {
        if (this.state.render_home) {
            return SupportVector;
        }
        else if (this.state.render_login) {
            return LoginForm;
        }
        else if (this.state.render_registration) {
            return RegisterForm;
        }
        else {
            return SupportVector;
        }
    },
  // call back: return side navigation
    getNavBar: function(type) {
        if (this.state.render_login || this.state.render_registration) {
            return 'span';
        }
        else {
            return NavBar;
        }
    },
  // display result
    render: function() {
        var SideBar = this.getNavBar();
        if (this.props.children) {
            var Content = 'span'
            var router_component = this.props.children;
        }
        else {
            var Content = this.getContent();
            var router_component = null;
        }

        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu onChange={this.setClickType} />
                </div>

                <div className='main'>
                    <NavBar />
                    <Content />
                    {router_component}
                </div>
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
