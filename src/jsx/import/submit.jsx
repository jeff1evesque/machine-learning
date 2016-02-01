/**
 * submit.jsx: append 'submit' button.
 *
 * @submit, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var Submit = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            ajax_done_result: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null
        };
    },
  // update 'state properties': allow parent component(s) to access properties
     formSubmit: function(event){
        this.props.onChange({result_form_submit: this.state.ajax_done_result});
     },
  // triggered when 'state properties' change
    render: function(){
        return(<input type='submit' className='svm-form-submit' onClick={this.formSubmit} />);
    },
  // call back: get session id(s) from server side, and append to form
    componentDidMount: function () {
      // ajax arguments
        var ajaxEndpoint = $(this).attr('action');
        var ajaxArguments = {
            'endpoint': ajaxEndpoint,
            'data': new FormData(this),
            'contentType': false,
            'processData': false,
        };

      // asynchronous callback: ajax 'done' promise
        ajaxCaller(function (asynchObject) {
        // Append to DOM
            if (asynchObject && asynchObject.error) {
                this.setState({ajax_done_error: asynchObject.error});
            } else if (asynchObject) {
                this.setState({ajax_done_result: asynchObject});
            }
            else {
                this.setState({ajax_done_result: null});
            }
        }.bind(this),
      // asynchronous callback: ajax 'fail' promise
        function (asynchStatus, asynchError) {
            if (asynchStatus) {
                this.setState({ajax_fail_status: asynchStatus});
                console.log('Error Status: ' + asynchStatus);
            }
            if (asynchError) {
                this.setState({ajax_fail_error: asynchError});
                console.log('Error Thrown: ' + asynchError);
            }
        }.bind(this),
      // pass ajax arguments
        ajaxArguments);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default Submit
