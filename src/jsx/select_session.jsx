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
            value: '--Select--',
            sent_form_data: false
        };
    },
  // update 'state properties'
    changeSessionType: function(event){
        this.setState({value: event.target.session_type});
        this.setState({submit: false});
    },
  // update 'state properties' from children component (i.e. 'render_submit')
    displaySubmitButton: function(event) {
        this.setState({submit: event.render_submit});
    },
    formSubmitted: function(event) {
        this.setState({sent_form_data: event.created_submit_button});
    },
  // triggered when 'state properties' change
    render: function(){
        var SessionType = this.getSessionType(this.state.session_type);
        {/* form submission button */}
        if (this.state.submit) {
            var SubmitButton = Submit;
        }
        else {
            var SubmitButton = 'span';
        }

        return(
            <form action='/load-data/' method='post'>
                <fieldset className='fieldset-session-type'>
                    <legend>Session Type</legend>
                    <p>Choose a session type</p>
                    <select name='svm_session' autoComplete='off' onChange={this.changeSessionType} value={this.state.session_type}>
                        <option value='' defaultValue>--Select--</option>
                        <option value='data_new'>New Data</option>
                        <option value='data_append'>Append Data</option>
                        <option value='model_generate'>Generate Model</option>
                        <option value='model_predict'>Make Prediction</option>
                    </select>
                </fieldset>


                {/* 'formResult' is accessible within child component as 'this.props.formResult' */}
                <SessionType onChange={this.displaySubmitButton} dataSent={this.state.sent_form_data} formObject={this} />
                <FormResponse formResult={this.state.result_form_response} />
                <SubmitButton onChange={this.formSubmitted} />
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
