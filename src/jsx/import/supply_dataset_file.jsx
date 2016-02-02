/**
 * supply_dataset_file.jsx: file upload fieldset.
 *
 * @SupplyDatasetFile, must be capitalized in order for reactjs to render it as
 *     a component. Otherwise, the variable is rendered as a dom node.
 *
 * @display_submit, a boolean value, defined via '!== 0'
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var SupplyDatasetFile = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            value: null,
            ajax_done_result: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null
        };
     },
  // update 'state properties': allow parent component(s) to access properties
    validStringEntered: function(event){
        this.props.onChange({display_submit: event.target.files.length !== 0});
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <div>
                <fieldset className='fieldset-supply-dataset'>
                    <legend>Supply Dataset</legend>
                    <input type='file' name='svm_dataset[]' className='svm-dataset-file' onChange={this.validStringEntered} value={this.state.value} />
                    <input type='button' value='Add more' className='add-element svm-dataset-file-add' />
                    <input type='button' value='Remove' className='remove-element svm-dataset-file-remove' />
                    <p className='form-note'>*<span className='bold'>Note:</span> Uploaded file(s) must be formatted as <span className='italic'>csv</span>, <span className='italic'>json</span>, or <span className='italic'>xml</span> format.</p>
                </fieldset>
            </div>
        );
    },
  // call back: get session id(s) from server side, and append to form
    componentDidMount: function () {
      // ajax arguments
        if (this.state.ajax_done_result) {
            var ajaxEndpoint = $(this).attr('action');
            var ajaxData = new FormData(this);
            var contentType = false;
            var processData = false;

            var ajaxArguments = {
                'endpoint': ajaxEndpoint,
                'data': new FormData(this.props.formObject),
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
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default SupplyDatasetFile
