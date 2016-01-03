/**
 * submit.jsx: append 'submit' button.
 *
 * @submit, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var Submit = React.createClass({
  // triggered when 'state properties' change
    render: function(){
        return(<input type='submit' class='svm-form-submit' />);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default Generate

// render a ReactElement into the DOM, in the supplied container
ReactDOM.render(<Submit />, document.querySelector('.ml-container form fieldset:last-of-type'));
