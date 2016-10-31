/**
 * menu_register.jsx: register menu markup.
 *
 * @MenuRegister, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var MenuRegister = React.createClass({
  // callback for register page
    clickRegister: function(event) {
      // prevent page reload
        event.preventDefault();

      // return state to parent component
        this.props.onChange({register: true});
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <a href='#'
                className='btn btn-primary'
                onClick={this.clickRegister}
            >
                Sign up
            </a>
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuRegister
