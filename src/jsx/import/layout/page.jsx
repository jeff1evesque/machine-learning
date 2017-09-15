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
      // default value: main content
        const home = content;

      // default value: css classnames
        if (css && !!css.type) {
            var css = css.type;
        }
        else {
            var css = 'container default';
        }

      // default value: layout style
        if (layout && !!layout.type) {
            var layout = layout.type;
        }
        else {
            var layout = 'default';
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
                            return <div>
                                <NavBar />
                                <AnalysisLayoutState />
                            </div>
                        </Route>
                    </Switch>
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
