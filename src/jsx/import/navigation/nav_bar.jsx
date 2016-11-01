/**
 * navbar.jsx: secondary menu..
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import { Router, Route, Link, browserHistory } from 'react-router'

var NavBar = React.createClass({
  // display result
    render: function() {
        return(
            <div className='side-menu'>
                <Link to={`/data_new`}><div className='menu-item'>Add new data</div></Link>
                <Link to={`/data_append`}><div className='menu-item'>Append data</div></Link>
                <Link to={`/model_generate`}><div className='menu-item'>Generate model</div></Link>
                <Link to={`/model_predict`}><div className='menu-item'>Make prediction</div></Link>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default NavBar
