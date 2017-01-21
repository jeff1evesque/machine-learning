/**
 * result-display.jsx: append form submission result.
 *
 * @ResultDisplay, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import React from 'react';
import checkValidString from './../validator/valid-string.js';
import checkValidFloat from './../validator/valid-float.js';

var ResultDisplay = React.createClass({
  // triggered when 'state properties' change
    render: function(){
      // variables
        var serverObj = this.props.formResult ? this.props.formResult : false;
        var resultSet = serverObj.result ? serverObj.result : false;
        var confidence = resultSet.confidence ? resultSet.confidence : false;
        var displayResult = false;
        var adjustedConfidence = false;

        if (
            serverObj && resultSet && resultSet.result &&
            checkValidString(resultSet.result)
        ) {
            var result = resultSet.result;
            displayResult = true;
        }

       // svm confidence measurements
        if (
            resultSet &&
            resultSet.model &&
            resultSet.model == 'svm' &&
            confidence &&
            confidence.classes &&
            confidence.classes.every(checkValidString) &&
            confidence.probability &&
            confidence.probability.every(checkValidFloat) &&
            confidence.decision_function &&
            confidence.decision_function.every(checkValidFloat)
        ) {
            adjustedConfidence = {
                'classes': confidence.classes.join(', '),
                'probability': confidence.probability.join(', '),
                'decision-function': confidence.decision_function.join(', ')
            }
        }

      // svr confidence measurements  
        else if (
            resultSet &&
            resultSet.model &&
            resultSet.model == 'svr' &&
            confidence &&
            confidence.score &&
            checkValidFloat(confidence.score)
        ) {
            adjustedConfidence = {
                'r^2': confidence.score
            }
        }

      // display result
        if (displayResult) {
            return(
                <fieldset className='fieldset-prediction-result'>
                    <legend>Prediction Result</legend>
                    <p className='result'>prediction: {result}</p>

                    {/* iterate dynamic object */}
                    {
                        adjustedConfidence &&
                        Object.keys(adjustedConfidence).map(function(key) {
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
