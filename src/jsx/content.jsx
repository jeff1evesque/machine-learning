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
  // display result
    render: function() {
        var navbar = this.renderNavBar();
        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu onChange={this.setClickType} />
                </div>

                <MainContent
                    renderNavBar={navbar}
                    renderChildren={this.props.children}
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
