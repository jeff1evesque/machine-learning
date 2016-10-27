/**
 * login.jsx: login form.
 *
 * @LoginForm, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import Spinner from '../general/spinner.jsx';

var LoginForm = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            display_spinner: false,
        };
    },
  // call back: used to return spinner
    getSpinner: function() {
        if (this.state.display_spinner) {
            return Spinner;
        }
        else {
            return 'span';
        }
    },
  // triggered when 'state properties' change
    render: function() {
        var AjaxSpinner = this.getSpinner();

        return(
            <div className='main-full-span login-form'>
                <form onSubmit={this.handleSubmit} ref='registerForm'>
                    <label>Username or email address</label>
                    <input
                        type='text'
                        name='user[login]'
                        className='input-block'
                        autoFocus
                    />
                    <label>Password</label>
                    <input
                        type='text'
                        name='user[password]'
                        className='input-block'
                    />

                    <input type="submit" className='input-submit' />
                    <AjaxSpinner />
                </form>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default LoginForm
