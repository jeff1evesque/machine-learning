/**
 * menu-register.jsx: register menu markup.
 *
 * @MenuRegister, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Link } from 'react-router';
import { connect } from 'react-redux';
import setPageState from './redux/action/page-action.jsx';

var MenuRegister = React.createClass({
  // call back: return register button
    renderContent: function() {
        if (
            this.props &&
            this.props.user &&
            this.props.user.name == 'anonymous'
        ) {
            return (
                <Link
                    to='/register'
                    activeClassName='active'
                    className='btn btn-primary'
                    onClick={this.menuClicked}
                >
                   <span>Sign up</span>
                </Link>
            );
        }
        else {
            return (<span />);
        }
    },
    menuClicked: function(event) {
      // update redux store
        var action = setPageState({layout: 'register'});
        this.props.dispatchPage(action);
    },
  // triggered when 'state properties' change
    render: function(){
        var selectedContent = this.renderContent();
        return(selectedContent);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuRegister
