
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
import PropTypes from 'prop-types';

class RegisterLink extends Component {
    // prob validation: static method, similar to class A {}; A.b = {};
    static propTypes = {
        user: PropTypes.shape({
            name: PropTypes.string.isRequired,
        }),
    }

    renderContent() {
        if (
            this.props &&
            this.props.user &&
            this.props.user.name == 'anonymous'
        ) {
            return (
                <NavLink
                    activeClassName='active'
                    className='btn btn-primary'
                    to='/register'
                >
                    <span>{'Sign up'}</span>
                </NavLink>
            );
        }
        return (<span />);
    }

    render() {
        const selectedContent = this.renderContent();
        return (selectedContent);
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default RegisterLink;
