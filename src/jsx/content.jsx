/**
 * user_menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import SupportVector from './support_vector.jsx';
import UserMenu from '/user_menu.jsx';

var Content = React.createClass({
  // display result
    render: function() {
        return(
            <div className='menu-container'>
                <UserMenu />
            </div>
            <div className='main'>
                <div className='navBar'></div>
                <div className='content'>
                    <SupportVector />
                </div>
            </div>
        );
    }
});

// render form
ReactDOM.render(<Content/>, document.querySelector('.container'));
