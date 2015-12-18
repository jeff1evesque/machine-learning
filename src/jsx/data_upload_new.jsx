/**
 * data_upload_new.jsx: append 'data_upload' fieldset.
 *
 * @Data_Upload_New, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var Data_Upload_New = React.createClass({
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
            <fieldset class='fieldset-session-data-upload'>
                <legend>Data Upload</legend>
                <fieldset class='fieldset-dataset-type'>
                    <legend>Configurations</legend>
                    <p>Please save the <i>Session Name</i>, then provide dataset type</p>
                    <input type='text' name='svm_title' placeholder='Session Name'>
                    <select name='svm_dataset_type' autoComplete='off' onChange={this.change} value={this.state.value}>
                        <option value='' defaultValue>--Select--</option>
                        <option value='file_upload'>Upload file</option>
                        <option value='dataset_url'>Dataset URL</option>
                    </select>
                </fieldset>
            </fieldset>
        );
    }
});

// render a ReactElement into the DOM, in the supplied container
$(document).ready(function() {
    ReactDOM.render(<Data_Upload_New />, document.querySelector('.fieldset-session-type'));
});
