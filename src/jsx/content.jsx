/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import ReactDOM from 'react-dom';
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
                    <NavBar />
                    {this.props.children}
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
    <AppRouter indexRoute={Page} renderSubpage={this.state.render_subpage} />,
    document.querySelector('.container')
);
