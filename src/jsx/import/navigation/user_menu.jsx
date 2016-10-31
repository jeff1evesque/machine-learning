/**
 * user_menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import MenuHome from './menu-items/menu_home.jsx';
import MenuLogin from './menu-items/menu_login.jsx';
import MenuRegister from './menu-items/menu_register.jsx';

var UserMenu = React.createClass({
  // return state to parent component
    displayHome: function(event) {
        this.props.onChange({home: event.home});
    },
  // return state to parent, and current component
    displayLogin: function(event) {
      // return state to parent component
        this.props.onChange({login: event.login});

      // conditionally define state(s)
        if (event.login) {
            this.setState({show_login: false});
            this.setState({show_register: false});
        }
        else {
            this.setState({show_login: true});
            this.setState({show_register: true});
        }
    },
  // return state to parent component
    displayRegister: function(event) {
        this.props.onChange({home: event.register});
    },
  // display result
    render: function() {
        var AjaxSpinner = this.getSpinner();
        if (this.state.show_login) {
            var Login = MenuLogin
        }
        else {
            var Login = 'span'
        }
        if (this.state.show_register) {
            var Register = MenuRegister
        }
        else {
            var Register = 'span'
        }

        {/* return:
            @classRegister, is accessible within child component as
                'this.props.classRegister'
            @classLogin, is accessible within child component as
                'this.props.classLogin'
        */}
        return(
            <nav className='main-navigation {this.state.home_class}'>
                <MenuHome
                    onChange={this.displayHome}
                    classRegister={this.state.show_register}
                    classLogin={this.state.show_login}
                />
                <Login onChange={this.displayLogin} />
                <Register onChange={this.displayRegister} />
            </nav>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default UserMenu
