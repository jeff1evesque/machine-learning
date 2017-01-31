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
        this.props.onChange({show_button: true});
    },
    componentDidMount: function() {
        if (
            loadState('username') &&
            String(loadState('username')) != 'anonymous'
        ) {
          // update component states
            this.setState({show_button: false});

          // update redux store
            var action = setLoginState();
            this.props.dispatch(action);
        }
        else {
          // update component states
            this.setState({show_button: true});
        }
    },
  // call back: return side navigation
    renderContent: function() {
        if (this.props.show_button) {
            return <Link
                       to='/register'
                       activeClassName='active'
                       className='btn btn-primary'
                       onClick={this.menuClicked}
                   >
                       <span>Sign up</span>
                   </Link>
        }
        else {
            return 'span';
        }
    },
  // triggered when 'state properties' change
    render: function(){
        var selectedContent = this.renderContent();

        return(
            {selectedContent}
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuRegister
