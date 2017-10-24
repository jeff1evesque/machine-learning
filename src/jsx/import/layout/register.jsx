/**
 * register.jsx: general register layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import React from 'react';
import RegisterState from '../redux/container/register.jsx';

const RegisterLayout = () =>
    (
        <div className="main-full-span register-form">
            <h1>Create your account</h1>
            <RegisterState />
        </div>
    );

// indicate which class can be exported, and instantiated via 'require'
export default RegisterLayout;
