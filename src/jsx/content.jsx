/**
 * content.jsx: generate main content.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import SupportVector from './import/content/support_vector.jsx';
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
  // display result
    render: function() {
        return(
            <div className='container-inner'>
                <div className='menu-container'>
                    <UserMenu onChange={this.setClickType} />
                </div>
                <div className='main'>
                    <div className='navBar'></div>
                    <div className='content'>
                        <SupportVector />
                    </div>
                </div>
            </div>
        );
    }
});

// render form
ReactDOM.render(<Content/>, document.querySelector('.container'));
