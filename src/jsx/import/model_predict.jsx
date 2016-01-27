/**
 * model_predict.jsx: append 'model_predict' fieldset.
 *
 * @ModelPredict, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var ModelPredict = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value: '--Select--',
            render_submit: false,
            ajax_done_options: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null
        };
    },
  // update 'state properties'
    changeModelId: function(event){
        if (event.target.value) {
            this.setState({value_model_id: event.target.value});
        }
        else {
            this.setState({value_model_id: '--Select--'});
            this.props.onChange({render_submit: false});
        }
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <fieldset className='fieldset-session-predict'>
                <legend>Analysis</legend>
                <fieldset className='fieldset-dataset-type'>
                    <legend>Configurations</legend>
                    <p>Select a previous model to analyze</p>
                    <select name='svm_model_id' autoComplete='off' onChange={this.changeModelId} value={this.state.value}>
                        <option value='' defaultValue>--Select--</option>
                    </select>
                </fieldset>
            </fieldset>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ModelPredict
