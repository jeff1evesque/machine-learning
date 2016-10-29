/**
 * menu_login.jsx: login menu markup.
 *
 * @MenuLogin, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var MenuHome = React.createClass({
  // callback for login page
    clickLogin: function(event) {
      // prevent page reload
        event.preventDefault();

      // return state to parent component
        this.props.onChange({login: true});
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <a href='#'
                className='btn mn-2'
                onClick={this.clickLogin}
            >
                Sign in
            </a>
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuLogin
