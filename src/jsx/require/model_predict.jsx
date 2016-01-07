/**
 * model_predict.jsx: append 'model_predict' fieldset.
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
        this.setState({value: event.target.value});
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <fieldset className='fieldset-session-predict'>
                <legend>Analysis</legend>
                <fieldset className='fieldset-dataset-type'>
                    <legend>Configurations</legend>
                    <p>Select a previous model to analyze</p>
                    <select name='svm_model_id' autoComplete='off' onChange={this.change} value={this.state.value}>
                        <option value='' defaultValue>--Select--</option>
                    </select>
                </fieldset>
            </fieldset>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default Model_Predict
