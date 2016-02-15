/**
 * data_upload_append.jsx: append 'data_upload' fieldset.
 *
 * @DataUploadAppend, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import checkValidInt from './import/validator/valid_int.js';
import checkValidString from './import/validator/valid_string.js';

var DataUploadAppend = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_session_id: '--Select--',
            value_dataset_type: '--Select--'
        };
    },
  // update 'state properties'
    changeSessionId: function(event){
        var sessionId = event.target.value_session_id;
        if (checkValidInt(sessionId)) {
            this.setState({
                value_session_id: sessionId
            });
        }
    },
    changeDatasetType: function(event){
        var datasetType = event.target.value_dataset_type;
        if (checkValidString(datasetType)) (
            this.setState({
                value_dataset_type: datasetType
            });
        }
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <fieldset className='fieldset-session-data-upload'>
                <legend>Data Upload</legend>
                <fieldset className='fieldset-dataset-type'>
                    <legend>Configurations</legend>
                    <p>Select past session, and upload type</p>
                    <select name='svm_session_id' autoComplete='off' onChange={this.changeSessionId} value={this.state.value_session_id}>
                        <option value='' defaultValue>--Select--</option>
                    </select>
                    <select name='svm_dataset_type' autoComplete='off' onChange={this.changeDatasetType} value={this.state.value_dataset_type}>
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
export default DataUploadAppend
