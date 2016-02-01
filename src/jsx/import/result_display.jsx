/**
 * result_display.jsx: append form submission result.
 *
 * @ResultDisplay, must be capitalized in order for reactjs to render it as a
 *     component. Otherwise, the variable is rendered as a dom node.
 *
 * Note: this script implements jsx (reactjs) syntax.
 */

var ResultDisplay = React.createClass({
  // initial 'state properties'
    getInitialState: function() {
        return {
            ajax_done_result: null,
            ajax_done_error: null,
            ajax_fail_error: null,
            ajax_fail_status: null
        };
    },
  // triggered when 'state properties' change
    render: function(){
        var result = this.props.formResult;

        return(
            <fieldset className='fieldset-prediction-result'>
                <legend>Prediction Result</legend>
                <p className='result'>{result}</p>
            </fieldset>
        );
        return(<input type='submit' className='svm-form-submit' onClick={this.formSubmit} />);
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default ResultDisplay
