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
import HomePage from './content/home-page.jsx';
import UserMenu from './navigation/user-menu.jsx';

var PageLayout = React.createClass({
  // display result
    render: function() {
      // destructure router object
        if (this.props && !!this.props.MainContent) {
            var MainContent = this.props.MainContent;
        }
        else {
            var MainContent = HomePage;
        }

        if (this.props && !!this.props.UserMenu) {
            var UserMenu = this.props.UserMenu;
        }
        else {
            var UserMenu = UserMenu;
        }

        if (this.props && !!this.props.SideBar) {
            var SideBar = this.props.SideBar;
        }
        else {
            var SideBar = 'span';
        }

        if (this.props && !!this.props.css) {
            var css = this.props.css;
        }
        else {
            var css = 'main-full-span home';
        }

        if (this.props && !!this.props.layout) {
            var layout = this.props.layout;
        }
        else {
            var layout = 'home';
        }

      // render content
        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu layout={layout}/>
                </div>
                <div className='main'>
                    <SideBar />
                    <div className={css}>
                        <MainContent />
                    </div>
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
