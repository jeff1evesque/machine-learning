/**
 * data_append.jsx: append 'data_append' fieldset.
 *
 * @DataAppend, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 * @sessionId, pass a callback to be run, within the corresponding ajax script.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import SupplyDatasetFile from './supply_dataset_file.jsx';
import SupplyDatasetUrl from './supply_dataset_url.jsx';

var DataAppend = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_session_id: '--Select--',
            value_dataset_type: '--Select--'
        };
    },
  // update 'state properties'
    changeSessionId: function(event){
        if (event.target.value) {
            this.setState({value_session_id: event.target.value});
        }
        else {
            this.props.onChange({render_submit: false});
        }
    },
    changeDatasetType: function(event){
        if (event.target.value) {
            this.setState({value_dataset_type: event.target.value});
        }
        else {
            this.props.onChange({render_submit: false});
        }
    },
  // update 'state properties' from children component (i.e. 'validStringEntered')
    displaySubmit: function(event) {
        if (event.display_submit) {
            this.props.onChange({render_submit: event.display_submit});
        }
        else {
            this.props.onChange({render_submit: false});
        }
    },
  // triggered when 'state properties' change
    render: function(){
        var SupplyDataset = this.getSupplyDataset();
        var SessionId = this.getSessionId();

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

                <SupplyDataset onChange={this.displaySubmit}/>
            </fieldset>
        );
    },
  // call back: used for the above 'render' (return 'span' if undefined)
    getSupplyDataset: function() {
        if (typeof this.state.value_title === 'string' && String(this.state.value_title).length > 0) {
            return {
                file_upload: SupplyDatasetFile,
                dataset_url: SupplyDatasetUrl
            }[this.state.value_dataset_type] || 'span';
        }
        else {
            return 'span';
        }
    }
  // call back: acquire session id from server side, and append to form
    getSessionId: function () {
        var sessionId = sessionId(function (sessionId) {

            // Append stored session id instances
            if (sessionId.error) {
                $('.fieldset-dataset-type').append('<div class="error">' + sessionId.error + '</div>');
                $('.fieldset-select-model').append('<div class="error">' + sessionId + '</div>');
            } else {
                $.each(sessionId, function(index, value) {
                    var valueId    = value.id;
                    var valueTitle = value.title;
                    var element    = '<option ' + 'value="' + valueId + '">' + valueId + ': ' + valueTitle + '</option>';

                    $('select[name="svm_session_id"]').append(element);
                });
            }

        }
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default DataAppend
