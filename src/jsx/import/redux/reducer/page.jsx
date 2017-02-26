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

  // assign elements from action
    switch(action.type) {
        case 'SUBMIT-SV-ANALYSIS':
            if (action && action.button && !!action.button.submit_analysis) {
                var submitButtonAnalysis = action.button.submit_analysis;

                return {
                    ...state,
                    status: 'default',
                    button: {
                        ...state.button,
                        submit_analysis: submitButtonAnalysis
                    }
                }
            }
        case 'GOTO-RESULTS':
            if (action && action.button && !!action.button.goto_results) {
                var gotoResults = action.button.goto_results;

                return {
                    ...state,
                    status: 'default',
                    button: {
                        ...state.button,
                        ...submit_analysis: gotoResults
                   }
                }
            }
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default page
