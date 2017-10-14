/**
 * page.jsx: describe page attributes.
 *
 * Note: the triple dots is the 'object spread' syntax:
 *
 *       http://redux.js.org/docs/recipes/UsingObjectSpreadOperator.html
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

const page = (state='default', action) => {
    var submitButtonAnalysis = false;
    var gotoResults = false;
    var spinner = false;

  // assign elements from action
    switch(action.type) {
        case 'SET-RESULTS-BUTTON':
            var reviewResults = action.button.review_results;

            return {
                ...state,
                button: {
                    ...state.button,
                    review_results: reviewResults
                }
            }
        case 'SUBMIT-SV-ANALYSIS':
            var submitButtonAnalysis = action.button.submit_analysis;

            return {
                ...state,
                status: 'default',
                button: {
                    ...state.button,
                    submit_analysis: submitButtonAnalysis
                }
            }
        case 'GOTO-RESULTS':
            var gotoResults = action.button.goto_results;

            return {
                ...state,
                status: 'default',
                button: {
                    ...state.button,
                    goto_results: gotoResults
                }
            }
        case 'SET-CONTENT-TYPE':
            var contentType = action.content_type;

            return {
                ...state,
                content_type: contentType
            }
        case 'SET-SPINNER':
            var spinnerBool = action.spinner;

            return {
                ...state,
                effects: {
                    ...state.effects,
                    spinner: spinnerBool
                }
            }
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default page
