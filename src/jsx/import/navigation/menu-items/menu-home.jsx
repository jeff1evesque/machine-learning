/**
 * menu-home.jsx: home menu markup.
 *
 * @MenuHome, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import { Link } from 'react-router'
import SvgHome from '../../svg/svg-home.jsx';
import setPageState from './redux/action/page-action.jsx';

var MenuHome = React.createClass({
    menuClicked: function(event) {
      // update redux store
        var action = setPageState({layout: 'home'});
        this.props.dispatchPage(action);
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <Link
                to='/'
                activeClassName='active'
                className='icon home'
                onClick={this.menuClicked}
            >
                <SvgHome />
            </Link>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuHome
