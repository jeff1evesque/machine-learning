/**
 * data_new.jsx: append 'data_new' fieldset.
 *
 * @DataNew, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import SupplyDatasetFile from './supply_dataset_file.jsx';
import SupplyDatasetUrl from './supply_dataset_url.jsx';

var DataNew = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_title: null,
            value_dataset_type: '--Select--',
            render_submit: false
        };
    },
  // update 'state properties'
    changeDatasetType: function(event){
        if (event.target.value) {
            this.setState({value_dataset_type: event.target.value});
        }
        else {
            this.setState({value_dataset_type: '--Select--'});
            this.props.onChange({render_submit: false});
        }
    },
    changeTitle: function(event){
        if (event.target.value) {
            this.setState({value_title: event.target.value});
        }
        else {
            this.setState({value_title: null});
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
        var inputDatasetType = this.state.value_dataset_type;
        var inputTitle = this.state.value_title;
        var SupplyDataset = this.getSupplyDataset(inputDatasetType, inputTitle);

        return(
            <fieldset className='fieldset-session-data-upload'>
                <legend>Data Upload</legend>
                <fieldset className='fieldset-dataset-type'>
                    <legend>Configurations</legend>
                    <p>Please save the <i>Session Name</i>, then provide dataset type</p>
                    <input type='text' name='svm_title' placeholder='Session Name' onInput={this.changeTitle} value={this.state.value_title} />
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
    getSupplyDataset: function(datasetType, title) {
        if (typeof title === 'string' && String(title).length > 0) {
            return {
                file_upload: SupplyDatasetFile,
                dataset_url: SupplyDatasetUrl
            }[datasetType] || 'span';
        }
        else {
            return 'span';
        }
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default DataNew
