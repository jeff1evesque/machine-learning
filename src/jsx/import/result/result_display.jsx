/**
 * result_display.jsx: append form submission result.
 *
 * @ResultDisplay, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

import checkValidString from './../validator/valid_string.js';

var ResultDisplay = React.createClass({
  // triggered when 'state properties' change
    render: function(){
      // variables
        var serverObj = this.props.formResult ? this.props.formResult : false;
        var serverResult = serverObj.result ? serverObj.result : false;
        var displayResult = false;

        if (
            serverObj && serverResult && serverResult.result &&
            checkValidString(serverResult.result)
        ) {
            var result = serverResult.result;
            displayResult = true;
        }

      // display result
        if (displayResult) {
            return(
                <fieldset className='fieldset-prediction-result'>
                    <legend>Prediction Result</legend>
                    <p className='result'>{result}</p>
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
