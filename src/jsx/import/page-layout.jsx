/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 * Note: when destructuring objects, if the associated object was assigned
 *       null, undefined, false, or 0, the default values will not be set.
 *       However, if the associated object property does not exist, then during
 *       destructuring, it will be assigned the default value.
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
        if (!content && this.props.route.path == '/') {
            var content = HomePage;
        }
        else {
            var content = null;
        }

      // default value: css classnames
        if (css && !!css.key) {
            var css = css.key;
        }
        else {
            var css = 'main-full-span default';
        }

      // default value: layout style
        if (layout && !!layout.key) {
            var layout = layout.key;
        }
        else {
            var layout = 'default';
        }

      // render content
        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu layout={layout.key} />
                </div>
                <div className='main'>
                    {sidebar}
                    <div className={css.key}>
                        {content}
                    </div>
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
