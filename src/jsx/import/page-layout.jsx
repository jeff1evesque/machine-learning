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
  // callback: used to return spinner
    getLayout: function() {
      // local variables
        var layout = this.props.page.layout;

      // determine sidebar and css string
        if (layout == 'login') {
            var SideBar = 'span';
            var contentCSS = 'main-full-span login-form';
        }
        else if (layout == 'register') {
            var SideBar = 'span';
            var contentCSS = 'main-full-span register-form'
        }
        else if (layout == 'support-vector') {
            var SideBar = NavBar;
            var contentCSS = 'analysis-container';
        }
        else if (layout == 'home') {
            var SideBar = 'span';
            var contentCSS = 'main-full-span';
        }
        else {
            var SideBar = NavBar;
            var contentCSS = 'analysis-container';
        }

      // return sidebar and css string
        return {sidebar: SideBar, contentCSS: contentCSS}
    },
  // before component mounted
    componentWillMount: function() {
      // update redux store
        var action = setPageState({layout: 'home'});
        this.props.dispatchPage(action);
    },
  // display result
    render: function() {
      // local variables
        var getLayout = this.getLayout();
        var contentCSS = getLayout.contentCSS;
        var SideBar = getLayout.sidebar;

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
