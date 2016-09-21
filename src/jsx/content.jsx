/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import SupportVector from './import/content/support_vector.jsx';
import LoginForm from './import/content/login.jsx';
import RegisterForm from './import/content/register.jsx';
import UserMenu from './import/navigation/user_menu.jsx';

var Content = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            render_login: false,
            render_register: false,
        };
    },
  // update 'state properties'
    setClickType: function(event){
        var clickType = event.target;

        if (clickType && clickType.login) {
            this.setState({render_register: false});
            this.setState({render_login: true});
        }
        else if (clickType && clickType.register) {
            this.setState({render_login: false});
            this.setState({render_register: true});
        }
    },
  // call back: generate main content
    getContent: function(type) {
        if (this.state.login) {
            return LoginForm;
        }
        else if (this.state.register) {
            return RegisterForm;
        }
        else {
            return SupportVector;
        }
    }
  // display result
    render: function() {
        var Content = this.getContent();

        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu onChange={this.setClickType} />
                </div>
                <div className='main'>
                    <div className='navBar'></div>
                    <div className='content'>
                        <Content />
                    </div>
                </div>
            </div>
        );
    }
});

// render form
ReactDOM.render(<Content/>, document.querySelector('.container'));
