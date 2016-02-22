/**
 * supply_dataset_url.jss: url upload fieldset.
 *
 * @SupplyDatasetUrl, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import checkValidUrl from './../validator/valid_url.js';

var SupplyDatasetUrl = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value: null,
            additional_elements: []
        };
    },
  // update 'state properties': index for additional input elements
    handleAddMore: function(event){
        var elements = this.state.additional_elements;
        elements.push(true);
        this.setState({additional_elements: elements});
        this.props.onChange({submitted_proper_predictor: false});
    },
    handleRemove: function(event){
        var elements = this.state.additional_elements;
        var datasetBoolean = true;

        if (elements.length > 0) {
            elements.pop();
            this.setState({additional_elements: elements});

            for (index = 0; index < elements.length; index++) {
                if (this.state['value_dataset_' + index.toString()] === undefined) {
                    datasetBoolean = false;
                }
            }

            if (datasetBoolean) {
                this.props.onChange({submitted_proper_dataset: true});
            }
            else {
                this.props.onChange({submitted_proper_dataset: false});
            }
        }
    },
  // update 'state properties': allow parent component(s) to access properties
    validUrlEntered: function(){
        {/* get array of input elements, by classname */}
        var datasetNodeList = document.getElementsByClassName('svm-dataset-url');

        {/* if input value is a valid url, store 'true', within corresponding array */}
        var datasetArray = Array.prototype.map.call(datasetNodeList, function(element) {
            if (element.value && checkValidUrl(element.value)) {
                return true;
            }
            else {
                return false;
            }
        });

        {/* check if every element is 'true' */}
        var datasetBoolean = datasetArray.every(function(element) {
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
        var inputs = this.state.additional_elements;

        return(
            <fieldset className='fieldset-supply-dataset'>
                <legend>Supply Dataset</legend>
                <input type='url' name='svm_dataset[]' placeholder='Dataset URL' className='svm-dataset-url' onChange={this.validUrlEntered} value={this.state.value} />

                <input type='button' value='Add more' onClick={this.handleAddMore} />
                <input type='button' value='Remove' onClick={this.handleRemove} />

                {/* array components require unique 'key' value */}
                {inputs && inputs.map(function(value, index){ 
                    return <input type='url' name='svm_dataset[]' placeholder='Dataset URL' className='svm-dataset-url' key={index} onChange={this.validUrlEntered} value={this.state['value_dataset_' + index.toString()]} />;
                }.bind(this))}
            </fieldset>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default SupplyDatasetUrl
