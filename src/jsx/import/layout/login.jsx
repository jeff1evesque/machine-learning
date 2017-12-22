/**
 * login.jsx: general login layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import React from 'react';
import LoginState from '../redux/container/login.jsx';

const LoginLayout = () =>
    (
        <div className='login-form'>
            <LoginState />
        </div>
    );

// indicate which class can be exported, and instantiated via 'require'
export default LoginLayout;
