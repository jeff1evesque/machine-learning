/**
 * supply_predictors.jss: generate correct number of input elements, based on
 *     the number of generalized features, that can be expected for the
 *     selected dataset. When values are entered in the input element, a
 *     prediction can be estimated, and returned to the front-end.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var SupplyPredictors = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            ajax_done_options: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null
        };
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <fieldset class='fieldset-prediction-input'>
                <legend>Prediction Input</legend>


            </fieldset>
        );
    },
  // call back: get session id(s) from server side, and append to form
    componentDidMount: function () {
      // asynchronous callback: ajax 'done' promise
        featureProperties(function (asynchObject) {
        // Append to DOM
            if (asynchObject && asynchObject.error) {
                this.setState({ajax_done_error: asynchObject.error});
            } else if (asynchObject) {
                this.setState({ajax_done_options: asynchObject});
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
        }.bind(this));
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default SupplyPredictors
