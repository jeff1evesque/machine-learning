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
import HomePage from '../content/home-page.jsx';
import UserMenu from '../navigation/user-menu.jsx';
import AnalysisLayoutState from '../redux/container/analysis-layout.jsx';
import NavBar from '../navigation/nav-bar.jsx';

var PageLayout = React.createClass({
    render: function() {
      // destructure react-router
        var {
            content,
            sidebar,
            css,
            layout
        } = this.props;

      // default value: main content
        if (this.props.location.pathname == '/') {
            var content = <HomePage />;
        }
        else if (!content) {
            var content = null;
        }

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
                <Route
                    path='/session'
                    components={{
                        content: AnalysisLayoutState,
                        sidebar: NavBar,
                        css: 'container analysis-container',
                        layout: 'analysis'
                    }}
                />
                <div className='menu-container'>
                    <UserMenu layout={layout} />
                </div>
                <div className='main'>
                    {sidebar}
                    {content}
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
