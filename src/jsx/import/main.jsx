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
import LoginForm from './content/login.jsx';
import RegisterForm from './content/register.jsx';

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

var MainContent = React.createClass({
  // call back: return side navigation
    isNavBar: function() {
        if (this.props.renderNavBar) {
            return NavBar;
        }
        else {
            return <span />;
        }
    },
  // display result
    render: function() {
        var SideBar = this.isNavBar();
        console.log(this.props);

        if (
            this.props &&
            this.props.componentType == 'LoginLayout'
        ) {
            var ChildComponent = <LoginForm />;
        }
        else if (
            this.props &&
            this.props.componentType == 'RegisterLayout'
        ) {
            var ChildComponent = <RegisterForm />;
        }
        else if (
            this.props &&
            this.props.componentType == 'AnalysisLayout'
        ) {
            var sessionType = this.props.sessionType;
            var ChildComponent = <SvContainer displayName={sessionType} />;
        }
        else {
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
