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
import UserMenu from './navigation/user-menu.jsx';
import NavBar from './navigation/nav-bar.jsx';

var PageLayout = React.createClass({
  // display result
    render: function() {
        var layout = this.props.page.layout;
        if (layout == 'login') {
            var SideBar = 'span';
            var contentCSS = 'main-full-span login-form';
        }
        else if (this.props.layout == 'register') {
            var SideBar = 'span';
            var contentCSS = 'main-full-span register-form'
        }
        else if (this.props.layout == 'support-vector') {
            var SideBar = NavBar;
            var contentCSS = 'analysis-container';
        }
        else {
            var SideBar = NavBar;
            var contentCSS = 'main-full-span login-form';
        }

        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu layout={this.props.page.layout} />
                </div>

                <div className='main'>
                    <SideBar />
                    <div className={contentCSS}>
                        {this.props.children}
                    </div>
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
