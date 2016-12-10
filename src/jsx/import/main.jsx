/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import NavBar from './navigation/nav_bar.jsx';
import UserMenu from './navigation/user_menu.jsx';
import SupportVector from './content/support_vector.jsx';

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
        return(
            <div className='main'>
                <SideBar />
                {this.props.renderChildren}
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MainContent
