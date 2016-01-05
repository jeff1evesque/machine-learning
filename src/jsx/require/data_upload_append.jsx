/**
 * data_upload_append.jsx: append 'data_upload' fieldset.
 *
 * @Data_Upload_Append, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var Data_Upload_Append = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_session_id: '--Select--',
            value_dataset_type: '--Select--'
        };
    },
  // update 'state properties'
    change: function(event){
        this.setState({
            value_session_id: event.target.value_session_id,
            value_dataset_type: event.target.value_dataset_type
        });
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <fieldset className='fieldset-session-data-upload'>
                <legend>Data Upload</legend>
                <fieldset className='fieldset-dataset-type'>
                    <legend>Configurations</legend>
                    <p>Select past session, and upload type</p>
                    <select name='svm_session_id' autoComplete='off' onChange={this.change} value={this.state.value_session_id}>
                        <option value='' defaultValue>--Select--</option>
                    </select>
                    <select name='svm_dataset_type' autoComplete='off' onChange={this.change} value={this.state.value_dataset_value}>
                        <option value='' defaultValue>--Select--</option>
                        <option value='file_upload'>Upload file</option>
                        <option value='dataset_url'>Dataset URL</option>
                    </select>
                </fieldset>
            </fieldset>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default Data_Upload_Append

// render a ReactElement into the DOM, in the supplied container
ReactDOM.render(<Data_Upload_Append />, document.querySelector('.fieldset-session-type'));
