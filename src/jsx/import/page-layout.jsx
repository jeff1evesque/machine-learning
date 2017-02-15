/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 * Note: when destructuring an object, if the associated properties was
 *       assigned null, undefined, false, or 0, the default values will not be
 *       set. However, if the associated object property does not exist, then
 *       during destructuring, it will be assigned the default value.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import HomePage from './content/home-page.jsx';
import UserMenu from './navigation/user-menu.jsx';

var PageLayout = React.createClass({
    render: function() {
      // destructure router
        var {
            content,
            sidebar,
            css,
            layout
        } = this.props;

      // default value: main content
        if (!content && this.props.location.pathname == '/') {
            var content = HomePage;
        }
        else if (!content) {
            var content = null;
        }

      // default value: css classnames
        if (css && !!css.type) {
            var css = css.type;
        }
        else {
            var css = 'main-full-span default';
        }

      // default value: layout style
        if (layout && !!layout.type) {
            var layout = layout.type;
        }
        else {
            var layout = 'default';
        }

      // render content
        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu layout={layout.type} />
                </div>
                <div className='main'>
                    {sidebar}
                    <div className={css.type}>
                        {content}
                    </div>
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
