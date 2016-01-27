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

        };
    },
  // triggered when 'state properties' change
    render: function(){
        return(
            <fieldset class='fieldset-prediction-input'>
                <legend>Prediction Input</legend>


            </fieldset>
        );
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default SupplyPredictors
