/**
 * user_menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var UserMenu = React.createClass({
  // display result
    render: function() {
        return(
            <nav className='main-navigation'>
                <a href='/login' className='btn'>Sign in</a>
                <a href='/register' className='btn btn-primary'>Sign up</a>
            </nav>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default UserMenu
