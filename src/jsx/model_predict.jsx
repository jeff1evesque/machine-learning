/**
 * model_predict.jsx: append 'model_generate' fieldset.
 *
 * @Model_Predict, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var Model_Predict = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value: '--Select--'
        };
    },
  // update 'state properties'
    change: function(event){
        this.setState({
            this.setState({value: event.target.value});
        });
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <fieldset class='fieldset-session-predict'>
                <legend>Analysis</legend>
                <fieldset class='fieldset-dataset-type'>
                    <legend>Configurations</legend>
                    <p>Select a previous model to analyze</p>
                    <select name='svm_model_id'>
                        <option value='' defaultValue>--Select--</option>
                    </select>
                </fieldset>
            </fieldset>
        );
    }
});

// render a ReactElement into the DOM, in the supplied container
$(document).ready(function() {
    ReactDOM.render(<Model_Predict />, document.querySelector('.fieldset-session-type'));
});
