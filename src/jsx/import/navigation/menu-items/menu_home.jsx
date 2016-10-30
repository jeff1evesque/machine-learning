/**
 * menu_home.jsx: home menu markup.
 *
 * @MenuHome, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import SvgHome from '../../svg/svg_home.jsx';

var MenuHome = React.createClass({
  // callback for home page
    clickHome: function(event) {
      // prevent page reload
        event.preventDefault();

      // return state to parent component
        this.props.onChange({home: true});

      // conditional classname: defined from parent component
        if (this.props.classLogin || this.props.classRegister) {
            this.setState({css_options: 'not-centered'});
        }
        else {
            this.setState({css_options: 'centered'});
        }
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <a href='#'
                className={'icon home ' + this.state.css_options}
                onClick={this.clickHome}
            >
                <SvgHome />
            </a>
        )
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default MenuHome
