/**
 * model_generate.jsx: append 'model_generate' fieldset.
 *
 * @ModelGenerate, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var ModelGenerate = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_session_id: '--Select--',
            value_model_type: '--Select--',
            render_submit: false,
            ajax_done_options: null
        };
    },
  // update 'state properties'
    changeSessionId: function(event){
        if (event.target.value) {
            this.setState({value_session_id: event.target.value});
            dispatchSubmitButton();
        }
        else {
            this.setState({value_session_id: '--Select--'});
            this.props.onChange({render_submit: false});
        }
    },
    changeModelId: function(event){
        if (event.target.value) {
            this.setState({value_model_id: event.target.value});
            dispatchSubmitButton();
        }
        else {
            this.setState({value_model_type: '--Select--'});
            this.props.onChange({render_submit: false});
        }
    },
  // update 'state properties': allow parent component(s) to access properties
    dispatchSubmitButton: function(){
        var modelId = this.state.value_model_type;
        var sessionId = this.state.value_session_id;

        if (modelId != '--Select--' && Number(sessionId)) {
            this.props.onChange({render_submit: true});
        }
        else {
            this.props.onChange({render_submit: false});
        }
    },
  // triggered when 'state properties' change
    render: function(){
        var options = this.state.ajax_done_options;
        return(
            <fieldset className='fieldset-session-generate'>
                <legend>Generate Model</legend>
                <fieldset className='fieldset-select-model'>
                    <legend>Configurations</legend>
                    <p>Select past session, and model type</p>
                    <select name='svm_session_id' autoComplete='off' onChange={this.changeSessionId} value={this.state.value_session_id}>
                        <option value='' defaultValue>--Select--</option>

                        {/* array components require unique 'key' value */}
                        {options && options.map(function(value) {
                            return <option key={value.id} value={value.id}>{value.id}: {value.title}</option>;
                        })}

                    </select>
                    <select name='svm_model_type' autoComplete='off' onChange={this.changeModelId} value={this.state.value_model_type}>
                        <option value='' defaultValue>--Select--</option>
                        <option value='classification'>Classification</option>
                        <option value='regression'>Regression</option>
                    </select>
                </fieldset>
            </fieldset>
        );
    },
  // call back: get session id(s) from server side, and append to form
    componentDidMount: function () {
      // asynchronous callback: ajax 'done' promise
        sessionId(function (asynchObject) {
        // Append to DOM
            if (asynchObject && asynchObject.error) {
                this.setState({ajax_done_error: asynchObject.error});
            } else if (asynchObject) {
                this.setState({ajax_done_options: asynchObject});
            }
        }.bind(this),
      // asynchronous callback: ajax 'fail' promise
        function (asynchStatus, asynchError) {
            if (asynchStatus) {
                this.setState({ajax_fail_status: asynchStatus});
                console.log('Error Status: ' + asynchStatus);
            }
            if (asynchError) {
                this.setState({ajax_fail_error: asynchError});
                console.log('Error Thrown: ' + asynchError);
            }
        }.bind(this));
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ModelGenerate
