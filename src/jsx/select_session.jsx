/**
 * select_session.js: initial form.
 *
 * @SelectSession, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import ModelGenerate from './require/model_generate.jsx';
import ModelPredict from './require/model_predict.jsx';
import DataNew from './require/data_new.jsx';
import DataAppend from './require/data_append.jsx';
import DataUploadNew from './require/data_upload_new.jsx';
import DataUploadAppend from './require/data_upload_append.jsx';
import Submit from './require/submit.jsx';
import SupplyDatasetFile from './require/supply_dataset_file.jsx';
import SupplyDatasetUrl from './require/supply_dataset_url.jsx';

var SelectSession = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value: '--Select--'
        };
    },
  // update 'state properties'
    change: function(event){
        this.setState({value: event.target.value});
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <form action='/load-data/' method='post'>
                <fieldset className='fieldset-session-type'>
                    <legend>Session Type</legend>
                    <p>Choose a session type</p>
                    <select name='svm_session' autoComplete='off' onChange={this.change} value={this.state.value}>
                        <option value='' defaultValue>--Select--</option>
                        <option value='data_new'>New Data</option>
                        <option value='data_append'>Append Data</option>
                        <option value='model_generate'>Generate Model</option>
                        <option value='model_predict'>Make Prediction</option>
                    </select>
                    if (this.state.value === 'data_new') {
                        <DateNew/>
                    }
                    elseif (this.state.value === 'data_append') {
                        <DataAppend/>
                    }
                    elseif (this.state.value === 'model_generate') {
                        <ModelGenerate/>
                    }
                    elseif (this.state.value === 'model_predict') {
                        <ModelPredict/>
                    }
                </fieldset>
            </form>
        );
    }
});

// render form
ReactDOM.render(<SelectSession/>, document.querySelector('.ml-container'));
