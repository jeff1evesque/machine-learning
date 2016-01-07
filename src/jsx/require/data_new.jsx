/**
 * data_new.jsx: append 'data_new' fieldset.
 *
 * @Data_New, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var Data_New = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_dataset_type: '--Select--',
            value_title: null
        };
    },
  // update 'state properties'
    change: function(event){
        this.setState({
            value: event.target.value_dataset_type,
            value_title: event.target.value_title
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
                    <input type='text' name='svm_title' placeholder='Session Name' onChange={this.change} value={this.state.value} />
                    <select name='svm_dataset_type' autoComplete='off' onChange={this.change} value={this.state.value_dataset_type}>
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
export default Data_New
