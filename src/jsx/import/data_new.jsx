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
            value_title: '',
            value_dataset_type: '--Select--'
        };
    },
  // update 'state properties'
    changeDatasetType: function(event){
        this.setState({value_dataset_type: event.target.value});
    },
    changeTitle: function(event){
        this.setState({value_title: event.target.value});
    },
  // triggered when 'state properties' change
    render: function(){
        var SupplyDataset = this.getSupplyDataset();
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

                <SupplyDataset/>
            </fieldset>
        );
    },
  // call back: used for the above 'render' (return 'span' if undefined)
    getSupplyDataset: function() {
        if (typeof this.state.value_title !== 'undefined' && this.state.value_title.length > 0) {
            return {
                file_upload: SupplyDatasetFile,
                dataset_url: SupplyDatasetUrl
            }[this.state.value_dataset_type] || 'span';
        }
        else {
            return null;
        }
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default DataNew
