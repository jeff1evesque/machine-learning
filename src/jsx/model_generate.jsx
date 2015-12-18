/**
 * model_generate.js: append 'model_generate' fieldset.
 *
 * @Model_Generate, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var Model_Generate = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_session_id: '--Select--',
            value_model_type: '--Select--'
        };
    },
  // update 'state properties'
    change: function(event){
        this.setState({
            value_session_id: event.target.value_session_id,
            value_model_type: event.target.value_model_type
        });
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <fieldset class='fieldset-session-generate'>
                <legend>Generate Model</legend>
                <fieldset class='fieldset-select-model'>
                    <legend>Configurations</legend>
                    <p>Select past session, and model type</p>
                    <select name='svm_session_id' autoComplete='off' onChange={this.change} value={this.state.value_session_id}>
                        <option value='' defaultValue>--Select--</option>
                    </select>
                    <select name='svm_model_type' autoComplete='off' onChange={this.change} value={this.state.value_model_type}>
                        <option value='' defaultValue>--Select--</option>
                        <option value='classification'>Classification</option>
                        <option value='regression'>Regression</option>
                    </select>
                </fieldset>
            </fieldset>
        );
    }
});

// render a ReactElement into the DOM, in the supplied container
$(document).ready(function() {
    ReactDOM.render(<Model_Generate />, document.querySelector('.fieldset-session-type'));
});
