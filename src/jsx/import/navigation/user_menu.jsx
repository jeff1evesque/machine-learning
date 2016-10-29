/**
 * user_menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import MenuHome from 'menu-items/menu_home.jsx';
import MenuLogin from 'menu-items/menu_login.jsx';
import MenuRegister from 'menu-items/menu_register.jsx';

var UserMenu = React.createClass({
  // display result
    render: function() {
        var AjaxSpinner = this.getSpinner();

        return(
            <nav className='main-navigation {this.state.home_class}'>
                <MenuHome />
                <MenuLogin />
                <MenuRegister />
            </nav>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default UserMenu
