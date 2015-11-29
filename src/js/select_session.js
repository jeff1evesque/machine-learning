var select_session = React.createClass({
     getInitialState: function() {
         return {
             value: 'select'
         }
     },
     change: function(event){
         this.setState({value: event.target.value});
     },
     render: function(){
        return(
            <form action='/load-data/' method='post'>
                <fieldset class='fieldset-session-type'>
                    <legend>Session Type</legend>
                    <p>Choose a session type</p>
                    <select name='svm_session' autocomplete='off'>
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

React.render(<select_session />, document.getElementsByClassName('ml-container'));