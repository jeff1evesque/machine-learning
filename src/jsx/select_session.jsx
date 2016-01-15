/**
 * select_session.js: initial form.
 *
 * @SelectSession, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import ModelGenerate from './import/model_generate.jsx';
import ModelPredict from './import/model_predict.jsx';
import DataNew from './import/data_new.jsx';
import DataAppend from './import/data_append.jsx';
import DataUploadNew from './import/data_upload_new.jsx';
import DataUploadAppend from './import/data_upload_append.jsx';
import Submit from './import/submit.jsx';
import SupplyDatasetFile from './import/supply_dataset_file.jsx';
import SupplyDatasetUrl from './import/supply_dataset_url.jsx';

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
        var sessionType;

        if (this.state.value === 'data_new') {
            sessionType = <DataNew/>
        }
        elseif (this.state.value === 'data_append') {
            sessionType = <DataAppend/>
        }
        elseif (this.state.value === 'model_generate') {
            sessionType = <ModelGenerate/>
        }
        elseif (this.state.value === 'model_predict') {
            sessionType = <ModelPredict/>
        }

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

                    {sessionType}
                </fieldset>
            </form>
        );
    }
});

// render form
ReactDOM.render(<SelectSession/>, document.querySelector('.ml-container'));
