/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import SupportVector from './import/content/support_vector.jsx';
import LoginForm from './import/content/login.jsx';
import RegisterForm from './import/content/register.jsx';
import NavBar from './import/navigation/nav_bar.jsx';
import UserMenu from './import/navigation/user_menu.jsx';
import AppRouter from './router.jsx';

var Content = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            render_login: false,
            render_registration: false,
        };
    },
  // update 'state properties': click event has not 'target'
    setClickType: function(event){
        if (event.home) {
            this.setState({render_login: false});
            this.setState({render_registration: false});
            this.setState({render_home: true});
        }
        else if (event.login) {
            this.setState({render_home: false});
            this.setState({render_registration: false});
            this.setState({render_login: true});
        }
        else if (event.register) {
            this.setState({render_home: false});
            this.setState({render_login: false});
            this.setState({render_registration: true});
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
        var Content = this.getContent();

        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu onChange={this.setClickType} />
                </div>
                <div className='main'>
                    <SideBar />
                    <Content />
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
    <AppRouter indexRoute={Content} />,
    document.querySelector('.container')
);
