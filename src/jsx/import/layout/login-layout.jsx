/**
 * login-layout.jsx: general login layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import LoginState from '../redux/container/login-container.jsx';

var LoginLayout = React.createClass({
    render: function() {
        return(
            <div className='main-full-span login-form'>
                <LoginState />
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default LoginLayout
