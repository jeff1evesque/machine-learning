/**
 * page.jsx: general page layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import { Route } from 'react-router-dom';
import { Provider } from 'react-redux';
import UserMenu from '../navigation/user-menu.jsx';
import AnalysisLayoutState from '../redux/container/analysis-layout.jsx';
import NavBar from '../navigation/nav-bar.jsx';
import LoginLayout from './login.jsx';
import RegisterLayout from './register.jsx';

var PageLayout = React.createClass({
    render: function() {
      // default value: css classnames
        if (!!this.props && !!this.props.layout && !!this.props.layout.css) {
            const css = this.props.layout.css;
        }
        else {
            const css = 'container default';
        }

      // default value: layout style
        if (!!this.props && !!this.props.layout && !!this.props.layout.type) {
            const layout = this.props.layout.type;
        }
        else {
            const layout = 'default';
        }

        return(
            <div className={css}>
                <div className='menu-container'>
                    <UserMenu layout={layout} />
                </div>
                <div className='main'>
                    <Switch>
                        <Route exact path='/login' component={LoginLayout} />
                        <Route exact path='/logout' component={LoginLayout} />
                        <Route exact path='/register' component={RegisterLayout} />
                        <Route path='/session' render = {(props) => {
                            <div>
                                <NavBar />
                                <AnalysisLayoutState />
                            </div>
                        }} />
                    </Switch>
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
