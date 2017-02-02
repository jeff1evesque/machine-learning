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
import { loadState } from '../../redux/load-storage.jsx';
import setLoginState from '../../redux/action/login-action.jsx';

var MenuRegister = React.createClass({
  // return state to parent component
    menuClicked: function(event) {
        this.props.onChange({menu_clicked: 'register'});
    },
    componentDidUpdate: function() {
        if (
            this.props &&
            this.props.username &&
            this.props.username == 'anonymous' &&
            loadState('username') &&
            String(loadState('username')) != 'anonymous'
        ) {
          // update redux store
            var action = setLoginState();
            this.props.dispatch(action);
        }
    },
    componentWillMount: function() {
        if (
            this.props &&
            this.props.username &&
            this.props.username == 'anonymous' &&
            loadState('username') &&
            String(loadState('username')) != 'anonymous'
        ) {
          // update redux store
            var action = setLoginState();
            this.props.dispatch(action);
        }
    },
  // call back: return side navigation
    renderContent: function() {
        if (
            this.props &&
            this.props.username &&
            this.props.username == 'anonymous'
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
        else if (
            this.props === undefined ||
            this.props.username === undefined
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
  // triggered when 'state properties' change
    render: function(){
        var selectedContent = this.renderContent();

        return(selectedContent);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuRegister
