/**
 * data_append.jsx: append 'data_append' fieldset.
 *
 * @DataAppend, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 * @sessionId, pass a callback to be run, within the corresponding ajax
 *     script. This allows the server side to return a list of all stored
 *     session id's, and append them to the form, respectively.
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
            value_dataset_type: '--Select--',
            ajax_done_options: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null
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
    render: function(sessionId){
        var SupplyDataset = this.getSupplyDataset();
        var options = this.state.ajax_done_options;

        return(
            <fieldset className='fieldset-session-data-upload'>
                <legend>Data Upload</legend>
                <fieldset className='fieldset-dataset-type'>
                    <legend>Configurations</legend>
                    <p>Select past session, and upload type</p>
                    <select name='svm_session_id' autoComplete='off' onChange={this.changeSessionId} value={this.state.value_session_id}>
                        <option value='' defaultValue>--Select--</option>

                        {/* array components require unique 'key' value */}
                        {options && options.map(function(value) {
                            return <option key={value.id} value={value.id}>{value.id}: {value.title}</option>;
                        })}

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
export default DataAppend
