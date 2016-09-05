/**
 * result_display.jsx: append form submission result.
 *
 * @ResultDisplay, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import checkValidString from './../validator/valid_string.js';
import checkValidFloat from './../validator/valid_float.js';

var ResultDisplay = React.createClass({
  // triggered when 'state properties' change
    render: function(){
      // variables
        var serverObj = this.props.formResult ? this.props.formResult : false;
        var serverResult = serverObj.result ? serverObj.result : false;
        var confidence = serverResult.confidence ? serverResult.confidence : false;
        var displayResult = false;
        var adjustedConfidence = false;

        if (
            serverObj && serverResult && serverResult.result &&
            checkValidString(serverResult.result)
        ) {
            var result = serverResult.result;
            displayResult = true;
        }

        if (
            serverResult &&
            serverResult.model &&
            serverResult.model == 'svm' &&
            confidence.classes &&
//            confidence.classes.every(checkValidFloat) &&
            confidence.probability &&
//            confidence.probability.every(checkValidFloat) &&
            confidence.decision_function
//            confidence.decision_function.every(checkValidFloat)
        ) {
            console.log(confidence);
            adjustedConfidence = {
                'classes': confidence.classes.join(', '),
                'probability': confidence.probability.join(', '),
                'decision-function': confidence.decision_function.join(', ')
            }
        }

      // display result
        if (displayResult) {
            return(
                <fieldset className='fieldset-prediction-result'>
                    <legend>Prediction Result</legend>
                    <p className='result'>prediction: {result}</p>

                    {/* iterate dynamic object */}
                    {adjustedConfidence && Object.keys(adjustedConfidence).map(function(key) {
                        return <p key={key} className={key}>
                            {key}: {adjustedConfidence[key]}
                        </p>;
                    })}
                </fieldset>
            );
        }
        else {
            return(<span />);
        }
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ResultDisplay
