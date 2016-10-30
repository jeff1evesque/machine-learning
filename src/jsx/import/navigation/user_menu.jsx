/**
 * user_menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import MenuHome from 'menu-items/menu_home.jsx';
import MenuLogin from 'menu-items/menu_login.jsx';
import MenuRegister from 'menu-items/menu_register.jsx';

var UserMenu = React.createClass({
  // update 'state properties' from child component
    displayHome: function(event) {
        if (event.home) {
            this.props.onChange({home: event.home});
        }
        else {
            this.props.onChange({render_submit: false});
        }
    },
    displayLogin: function(event) {
        if (event.login) {
            this.props.onChange({login: event.login});
            this.setState({show_login: false});
            this.setState({show_register: false});
        }
        else {
            this.props.onChange({render_submit: false});
            this.setState({show_login: true});
            this.setState({show_register: true});
        }
    },
    displayRegister: function(event) {
        if (event.register) {
            this.props.onChange({home: event.register});
        }
        else {
            this.props.onChange({render_submit: false});
        }
    },
  // display result
    render: function() {
        var AjaxSpinner = this.getSpinner();
        if (this.state.show_login) {
            var Login = <MenuLogin />
        }
        else {
            var Login = 'span'
        }
        if (this.state.show_register) {
            var Register = <MenuRegister />
        }
        else {
            var Register = 'span'
        }

        {/* return:
            @classRegister, is accessible within child component as
                'this.props.show_register'
            @classLogin, is accessible within child component as
                'this.props.show_login'
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
