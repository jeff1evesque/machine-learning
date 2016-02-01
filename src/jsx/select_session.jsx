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
import ResultDisplay from './import/result_display.jsx';

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
        this.setState({submit: false});
    },
  // update 'state properties' from children component (i.e. 'render_submit')
    displaySubmit: function(event) {
        this.setState({submit: event.render_submit});
    },
  // get form response (after form submission)
    displayResult: function(event) {
        this.setState({result: event.result_form_response});
    }
  // triggered when 'state properties' change
    render: function(){
        var SessionType = this.getSessionType(this.state.value);
        {/* form submission button */}
        if (this.state.submit) {
            var SubmitButton = Submit;
        }
        else {
            var SubmitButton = 'span';
        }
        {/* form submission result */}
        if (this.state.result_form_response) {
            var FormResponse = ResultDisplay;
        }
        else {
            var FormResponse = 'span';
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
                </fieldset>

                {/* 'formResult' is accessible within child component as 'this.props.formResult' */}
                <SessionType onChange={this.displaySubmit} />
                <FormResponse formResult={this.state.result.form_response} />
                <SubmitButton onChange={this.displayResult} />
            </form>
        );
    },
  // call back: used for the above 'render' (return 'span' if undefined)
    getSessionType: function(type) {
        return {
            data_new: DataNew,
            data_append: DataAppend,
            model_generate: ModelGenerate,
            model_predict: ModelPredict
        }[type] || 'span';
    }
});

// render form
ReactDOM.render(<SelectSession/>, document.querySelector('.ml-container'));
