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
    render: function() {
      // destructure router: fallback with default values
        const {
            content=HomePage,
            sidebar='span',
            css='main-full-span default',
            layout='default'
        } = this.props;

      // render content
        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu layout={layout} />
                </div>
                <div className='main'>
                    {sidebar}
                    <div className={css}>
                        {content}
                    </div>
                </div>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default PageLayout
