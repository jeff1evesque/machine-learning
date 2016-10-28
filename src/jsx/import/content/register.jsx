/**
 * register.jsx: registration form.
 *
 * @RegisterForm, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import Spinner from '../general/spinner.jsx';

var RegisterForm = React.createClass({
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
            <div className='main-full-span register-form'>
                <form onSubmit={this.handleSubmit} ref='registerForm'>
                    <input
                        type='text'
                        name='user[login]'
                        className='input-block'
                        placeholder='Pick a username'
                    />
                    <input
                        type='text'
                        name='user[email]'
                        className='input-block'
                        placeholder='Your email address'
                    />
                    <input
                        type='text'
                        name='user[password]'
                        className='input-block'
                        placeholder='Create a password'
                    />

                    <input
                        type='submit'
                        className='btn btn-primary'
                    />
                    <AjaxSpinner />
                </form>
            </div>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default RegisterForm
