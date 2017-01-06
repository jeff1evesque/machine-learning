/**
 * menu_login.jsx: login menu markup.
 *
 * @MenuLogin, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Link } from 'react-router';
import { connect } from 'react-redux';
import { loadState } from '../../redux/load-storage.jsx';

const mapStateToProps = (state) => {
    return {
        username: state
    }
}

var MenuLogin = React.createClass({
  // return state to parent component
    menuClicked: function(event) {
        this.props.onChange({menu_clicked: 'login'});
    },
  // get login, logout button properties
    getButton: function() {
        if (loadState('username') != 'anonymous') {
            return {url: '/logout', text: 'Logout'};
        }
        else {
            return {url: '/login', text: 'Sign in'};
        }
    },
  // triggered when 'state properties' change
    render: function(){
      // local variables
        var url = this.getButton().url;
        var caption = this.getButton().text;

        return(
            <Link
                to={url}
                activeClassName='active'
                className='btn mn-2'
                onClick={this.menuClicked}
            >
                <span>{caption}</span>
            </Link>
        )
    }
});

const MenuLoginState = connect(
    mapStateToProps
)(MenuLogin)

// indicate which class can be exported, and instantiated via 'require'
export default MenuLoginState
