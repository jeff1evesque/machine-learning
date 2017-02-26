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

import assign from 'assign-deep';

const page = (state='default', action) => {
    var submitButtonAnalysis = false;
    var gotoResults = false;

    switch(action.type) {
        case 'SUBMIT-SV-ANALYSIS':
            if (action && action.button && !!action.button.submit_analysis) {
                var submitButtonAnalysis = action.button.submit_analysis;
            }

            return assign({}, state, {
                status: 'default',
                button: {
                    submit_analysis: submitButtonAnalysis
                }
            });
        case 'GOTO-RESULTS':
            if (action && action.button && !!action.button.goto_results) {
                var gotoResults = action.button.goto_results;
            }

            return assign({}, state, {
                status: 'default',
                button: {
                    goto_results: gotoResults
                }
            });
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default page
