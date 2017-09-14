/**
 * register.jsx: register link markup.
 *
 * @RegisterLink, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { NavLink } from 'react-router-dom';
import { connect } from 'react-redux';

var RegisterLink = React.createClass({
  // call back: return register button
    renderContent: function() {
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
        else {
            return (<span />);
        }
    },
  // triggered when 'state properties' change
    render: function(){
        var selectedContent = this.renderContent();
        return(selectedContent);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default RegisterLink
