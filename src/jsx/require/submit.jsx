/**
 * submit.jsx: append 'submit' button.
 *
 * @submit, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var Submit = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_session_id: '--Select--'
        };
    },
  // update 'state properties'
    change: function(event){
        this.setState({
            value_session_id: event.target.value_session_id
        });
    },
  // triggered when 'state properties' change
    render: function(){
        return(<input type='submit' class='svm-form-submit' />);
    }
});

// render a ReactElement into the DOM, in the supplied container
$(document).ready(function() {
    ReactDOM.render(<Submit />, document.querySelector('.ml-container form fieldset:last-of-type'));
});
