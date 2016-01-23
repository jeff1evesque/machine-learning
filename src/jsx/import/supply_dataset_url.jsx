/**
 * supply_dataset_url.jss: url upload fieldset.
 *
 * @SupplyDatasetUrl, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var SupplyDatasetUrl = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value: null
        };
    },
  // update 'state properties': allow parent component(s) to access properties
    validStringEntered: function(event){
        if (typeof event.target.value === 'string' && String(event.target.value).length > 0) {
            this.props.onChange({display_submit: true});
        }
        else {
            this.props.onChange({display_submit: false});
        }
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <fieldset className='fieldset-supply-dataset'>
                <legend>Supply Dataset</legend>
                <input type='url' name='svm_dataset[]' placeholder='Dataset URL' className='svm-dataset-xml' onChange={this.validStringEntered} value={this.state.value} />
                <input type='button' value='Add more' className='add-element svm-dataset-xml-add' />
                <input type='button' value='Remove' className='remove-element svm-dataset-xml-remove' />
            </fieldset>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default SupplyDatasetUrl
