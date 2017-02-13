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
import HomePage from './content/home-page.jsx';
import NavBar from './navigation/nav-bar.jsx';
import setPageState from './redux/action/page-action.jsx';

var PageLayout = React.createClass({
    componentWillMount: function() {
      // local variables
        var layout = this.props.page.layout;

      // assign layout
        this.setState({layout: layout});

      // determine sidebar and css string
        if (layout == 'login') {
            this.setState({sidebar: 'span'});
            this.setState({css: 'main-full-span login-form'});
            this.setState({home: 'span'});
        }
        else if (layout == 'register') {
            this.setState({sidebar: 'span'});
            this.setState({css: 'main-full-span register-form'});
            this.setState({home: 'span'});
        }
        else if (layout == 'support-vector') {
            this.setState({sidebar: NavBar});
            this.setState({css: 'analysis-container'});
            this.setState({home: 'span'});
        }
        else if (layout == 'home') {
            this.setState({sidebar: 'span'});
            this.setState({css: 'main-full-span home'});
            this.setState({home: HomePage});
        }
        else {
            this.setState({sidebar: 'span'});
            this.setState({css: 'main-full-span'});
            this.setState({home: HomePage});
        }

      // update redux store
        var action = setPageState({layout: 'home'});
        this.props.dispatchPage(action);
    },
  // display result
    render: function() {
        var SideBar = this.state.sidebar;
        var Home = this.state.home;

        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu layout={this.state.layout} />
                </div>

                <div className='main'>
                    <SideBar />
                    <div className={this.state.css}>
                        <Home />
                        {this.props.children}
                    </div>
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
