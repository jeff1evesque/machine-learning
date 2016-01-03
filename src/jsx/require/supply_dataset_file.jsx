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
            <fieldset class='fieldset-supply-dataset'>
                <legend>Supply Dataset</legend>
                <input type='file' name='svm_dataset[]' class='svm-dataset-file' onChange={this.change} value={this.state.value} />
                <input type='button' value='Add more' class='add-element svm-dataset-file-add' />
                <input type='button' value='Remove' class='remove-element svm-dataset-file-remove' />
                <p class='form-note'>*<span class='bold'>Note:</span> Uploaded file(s) must be formatted as <span class='italic'>csv</span>, <span class='italic'>json</span>, or <span class='italic'>xml</span> format.</p>
            </fieldset>
        );
     }
});

// indicate which class can be exported, and instantiated via 'require'
export default Upload_File

// render a ReactElement into the DOM, in the supplied container
ReactDOM.render(<Upload_File />, document.querySelector('.fieldset-dataset-type'));
