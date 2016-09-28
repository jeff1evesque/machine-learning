/**
 * user_menu.jsx: menu for logged-in, and anonymous users.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import SvgHome from '../general/spinner.jsx';

var UserMenu = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            home_hover: false,
        };
    },
  // call back: return home svg
    getSvgHome: function() {
        if (this.state.home_hover) {
            return SvgHome;
        }
        else {
            return 'span';
        }
    },
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
  // callback for mouseOver home svg
    mouseOverHome: function(event) {
        this.setState({home_hover: true});
    },
  // callback for mouseOut home svg
    mouseOutHome: function(event) {
        this.setState({home_hover: false});
    },
  // display result
    render: function() {
        var Home = this.getSvgHome();

        {/* return:
            @homeHover, is accessible within child component as
                'this.props.hover'
        */}
        return(
            <nav className='main-navigation'>
                <a href='#'
                   className='icon home'
                   onClick={this.clickHome}
                >
                    <Home onMouseOver={this.mouseOverHome}
                          onMouseOut={this.mouseOutHome}
                          hover={this.state.home_hover}
                    />
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
