/**
 * navbar.jsx: secondary menu..
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import { Link } from 'react-router'

var NavBar = React.createClass({
  // display result
    render: function() {
        return(
            <div className='side-menu'>
                <Link
                    to={`/data_new`}
                    activeClassName='active'
                    className='menu-item'
                >
                    Add new data
                </Link>

                <Link
                    to={`/data_append`}
                    activeClassName='active'
                    className='menu-item'
                >
                    Append data
                </Link>

                <Link
                    to={`/model_generate`}
                    activeClassName='active'
                    className='menu-item'
                >
                    Generate model
                </Link>

                <Link
                    to={`/model_predict`}
                    activeClassName='active'
                    className='menu-item'
                >
                    Make prediction
                </Link>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default NavBar
