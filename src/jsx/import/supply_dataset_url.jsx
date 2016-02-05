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
            value: null,
            input_index: 1
        };
    },
  // update 'state properties': index for additional input elements
    handleAddMore: function(event){
        this.state.input_index++;
    },
    handleRemove: function(event){
        if (this.state.input_index > 1) {
            this.state.input_index--;
        }
    },
  // update 'state properties': allow parent component(s) to access properties
    validUrlEntered: function(event){
        {/* get array of input elements, by classname */}
        var datasetNodeList = document.getElementsByClassName('svm-dataset-url');

        {/* if input value is empty, store 'false' within corresponding array */}
        var datasetArray = Array.prototype.map.call(datasetNodeList, function(element) {
            if (!element.value) {
                return false;
            }
            else {
                return true;
            }
        });

        {/* check if every element is 'true' */}
        var datasetBoolean = submitArray.every(function(element) {
            return element == true;
        });

        if (datasetBoolean) {
            this.props.onChange({submitted_proper_dataset: true});
        }
        else {
            this.props.onChange({submitted_proper_dataset: false});
        }
    },
  // triggered when 'state properties' change
    render: function(){
        var inputElements = this.state.array_input;

        return(
            <fieldset className='fieldset-supply-dataset'>
                <legend>Supply Dataset</legend>
                <input type='url' name='svm_dataset[]' placeholder='Dataset URL' className='svm-dataset-xml' onChange={this.validUrlEntered} value={this.state.value_dataset_0} />

                {/* array components require unique 'key' value */}
                {for (index = 0; this.state.input_index < index; index++) {
                    return <input type='url' name='svm_dataset[]' placeholder='Dataset URL' className='svm-dataset-url' key={index} onChange={this.validUrlEntered} value={this.state['value_dataset_' + index.toString()]} />;
                }.bind(this)}

                <input type='button' value='Add more' className='add-element svm-dataset-xml-add' onClick={handleAddMore} />
                <input type='button' value='Remove' className='remove-element svm-dataset-xml-remove' onClick={handleRemove} />
            </fieldset>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default SupplyDatasetUrl
