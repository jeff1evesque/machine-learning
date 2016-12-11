/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import NavBar from './navigation/nav_bar.jsx';
import UserMenu from './navigation/user_menu.jsx';

var MainContent = React.createClass({
  // display result
    render: function() {
        <div className='analysis-container'>
            <SupportVector routerProp={this.props.displayName} />
        </div>
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
        var SideBar = this.isNavBar();
        var childRoute = this.props.children.props.children.props.route;
        var sessionName = childRoute.component.displayName;

        if (childRoute.component == 'AnalysisLayout') {
            var ChildComponent = MainContent;
            var childAttribute = sessionName;
        }

        return(
            <div className='main'>
                <SideBar />
                <ChildComponent displayName={childAttribute} />
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MainContent
