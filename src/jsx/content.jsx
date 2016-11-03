/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import ReactDOM from 'react-dom';
import UserMenu from './import/navigation/user_menu.jsx';
import AppRouter from './router.jsx';

var Content = React.createClass({
    render: function() {
        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu />
                </div>
                <div className='main'>
                    {this.props.children}
                </div>
            </div>
        );
    }
});

// render form
//
// @indexRoute, is accessible within child component as 'this.props.indexRoute'
//
ReactDOM.render(
    <AppRouter indexRoute={Content} />,
    document.querySelector('.container')
);
