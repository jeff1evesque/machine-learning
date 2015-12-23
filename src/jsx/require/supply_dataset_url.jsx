/**
 * select_dataset_url.jss: url upload fieldset.
 *
 * @Upload_Url, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var Upload_Url = React.createClass({
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
                <input type='url' name='svm_dataset[]' placeholder='Dataset URL' class='svm-dataset-xml' onChange={this.change} value={this.state.value} />
                <input type='button' value='Add more' class='add-element svm-dataset-xml-add' />
                <input type='button' value='Remove' class='remove-element svm-dataset-xml-remove' />
            </fieldset>
        );
     }
});

// indicate which class can be exported, and instantiated via 'require'
export default Upload_Url

// render a ReactElement into the DOM, in the supplied container
$(document).ready(function() {
    ReactDOM.render(<Upload_Url />, document.querySelector('.fieldset-dataset-type'));
});
