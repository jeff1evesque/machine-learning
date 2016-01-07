/**
 * supply_dataset_file.jsx: file upload fieldset.
 *
 * @Upload_File, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var Upload_File = React.createClass({
  // initial 'state properties'
     getInitialState: function() {
         return {
             value: null
         };
     },
  // update 'state properties'
     change: function(event){
         this.setState({value: event.target.value});
     },
  // triggered when 'state properties' change
     render: function(){
        return(
            <fieldset className='fieldset-supply-dataset'>
                <legend>Supply Dataset</legend>
                <input type='file' name='svm_dataset[]' className='svm-dataset-file' onChange={this.change} value={this.state.value} />
                <input type='button' value='Add more' className='add-element svm-dataset-file-add' />
                <input type='button' value='Remove' className='remove-element svm-dataset-file-remove' />
                <p className='form-note'>*<span className='bold'>Note:</span> Uploaded file(s) must be formatted as <span className='italic'>csv</span>, <span className='italic'>json</span>, or <span className='italic'>xml</span> format.</p>
            </fieldset>
        );
     }
});

// indicate which class can be exported, and instantiated via 'require'
export default Upload_File
