/**
 * user_menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var UserMenu = React.createClass({
  // callback for home page
    clickHome: function(event) {
      // prevent page reload
        event.preventDefault();

      // return state to parent component
        this.props.onChange({home: true});
    },
  // callback for login page
    clickLogin: function(event) {
      // prevent page reload
        event.preventDefault();

      // return state to parent component
        this.props.onChange({login: true});
    },
  // callback for register page
    clickRegister: function(event) {
      // prevent page reload
        event.preventDefault();

      // return state to parent component
        this.props.onChange({register: true});
    },
  // display result
    render: function() {
        return(
            <nav className='main-navigation'>
                <a href='#'
                   className='icon home'
                   onClick={this.clickHome}
                >
                    <img src='static/img/home.svg' alt='Home' />
                </a>
                <a href='#'
                   className='btn mn-2'
                   onClick={this.clickLogin}
                >
                    Sign in
                </a>
                <a href='#'
                   className='btn btn-primary'
                   onClick={this.clickRegister}
                >
                    Sign up
                </a>
            </nav>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default UserMenu
