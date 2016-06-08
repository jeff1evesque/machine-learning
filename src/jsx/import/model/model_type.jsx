/**
 * model_type.jsx: append list of model types.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import checkValidString from './../validator/valid_string.js';

var ModelType = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value_model_type: '--Select--'
        };
    },
  // update 'state properties'
    changeModelType: function(event){
        if checkValidString(event.target.value) {
            this.props.onChange({modelType: this.state.value_model_type});
        }
        else {
            this.props.onChange({modelType: null});
        }
    },
  // triggered when 'state properties' change
    render: function(){
      // display result
        return(
            <select
                name='svm_model_type'
                autoComplete='off'
                onChange={this.changeModelType}
                value={this.state.value_model_type}
            >

                <option value='' defaultValue>--Select--</option>
                <option value='classification'>Classification</option>
                <option value='regression'>Regression</option>

            </select>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ModelType
