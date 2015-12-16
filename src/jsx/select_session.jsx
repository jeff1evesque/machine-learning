/**
 * select_session.js: initial form.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var select_session = React.createClass({
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
                <fieldset class='fieldset-session-type'>
                    <legend>Session Type</legend>
                    <p>Choose a session type</p>
                    <select name='svm_session' autocomplete='off' onChange={this.change} value={this.state.value}>
                        <option value='' selected='selected'>--Select--</option>
                        <option value='data_new'>New Data</option>
                        <option value='data_append'>Append Data</option>
                        <option value='model_generate'>Generate Model</option>
                        <option value='model_predict'>Make Prediction</option>
                    </select>
                </fieldset>
            </form>
        );
     }
});

// render a ReactElement into the DOM, in the supplied container
$( document ).ready(function() {
    ReactDOM.render(<select_session />, document.getElementsByClassName('ml-container'));
});
