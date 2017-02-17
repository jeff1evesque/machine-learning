/**
 * login-layout.jsx: general register layout.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import React from 'react';
import ReactDOM from 'react-dom';
import RegisterState from '../redux/container/register-container.jsx';

var RegisterLayout = React.createClass({
    render: function() {
        return(
            <div className='main-full-span register-form'>
                <RegisterState />
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default RegisterLayout
