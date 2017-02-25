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

import merge from 'assign-deeply';

const page = (state='default', action) => {
    var submitButtonAnalysis = false;
    var gotoResults = false;

    if (
        action &&
        action.button
    ) {
        var submitButtonAnalysis = !!action.button.submit_analysis ? true : false;
        var gotoResults = !!action.button.goto_results ? true : false;
    }

    switch(action.type) {
        case 'SUBMIT-SV-ANALYSIS':
            return merge(state, {
                status: 'default',
                button: {
                    submit_analysis: submitButtonAnalysis
                }
            });
        case 'GOTO-RESULTS':
            return merge(state, {
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
