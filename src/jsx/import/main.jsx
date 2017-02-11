/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import NavBar from './navigation/nav-bar.jsx';
import UserMenu from './navigation/user-menu.jsx';
import SupportVector from './content/support-vector.jsx';
import LoginState from './redux/container/login-container.jsx';
import RegisterState from './redux/container/register-container.jsx';

var SvContainer = React.createClass({
  // display result
    render: function() {
        return(
            <div className='analysis-container'>
                <SupportVector routerProp={this.props.displayName} />
            </div>
        );
    }
});

var LoginLayout = React.createClass({
  // display result
    render: function() {
        return(
            <div className='main-full-span login-form'>
                <LoginState />
            </div>
        );
    }
});

var RegisterLayout = React.createClass({
  // display result
    render: function() {
        return(
            <div className='main-full-span register-form'>
                <RegisterState />
            </div>
        );
    }
});

var MainContent = React.createClass({
  // call back: return side navigation
    isNavBar: function() {
        if (this.props.renderNavBar) {
            return NavBar;
        }
        else {
            return 'span';
        }
    },
  // display result
    render: function() {
        if (
            this.props &&
            this.props.layout == 'login'
        ) {
            var SideBar = 'span';
            var ChildComponent = <LoginLayout />;
        }
        else if (
            this.props &&
            this.props.layout == 'register'
        ) {
            var SideBar = 'span';
            var ChildComponent = <RegisterLayout />;
        }
        else if (
            this.props &&
            this.props.layout == 'support-vector'
        ) {
            var SideBar = this.isNavBar();
            var ChildComponent = <SvContainer />;
        }
        else {
            var SideBar = this.isNavBar();
            var ChildComponent = <SvContainer />;
        }

        return(
            <div className='main'>
                <SideBar />
                {ChildComponent}
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MainContent
