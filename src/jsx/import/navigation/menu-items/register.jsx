
/**
 * register.jsx: register link markup.
 *
 * @RegisterLink, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React, { Component } from 'react';
import { NavLink } from 'react-router-dom';
import { connect } from 'react-redux';

class RegisterLink extends Component {
    // call back: return register button
    renderContent() {
        if (
            this.props &&
            this.props.user &&
            this.props.user.name == 'anonymous'
        ) {
            return (
                <NavLink
                    to='/register'
                    activeClassName='active'
                    className='btn btn-primary'
                >
                    <span>Sign up</span>
                </NavLink>
            );
        }
        return (<span />);
    }
    // triggered when 'state properties' change
    render() {
        const selectedContent = this.renderContent();
        return (selectedContent);
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default RegisterLink;
