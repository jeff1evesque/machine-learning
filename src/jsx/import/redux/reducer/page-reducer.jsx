/**
 * page-reducer.jsx: describe page attributes.
 *
 * Note: the triple dots is the 'object spread' syntax:
 *
 *       http://redux.js.org/docs/recipes/UsingObjectSpreadOperator.html
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import 'core-js/modules/es6.object.assign';

const page = (state='default', action) => {
    if (
        action &&
        action.submit_button &&
        !!action.submit_button.analysis
    ) {
        var submitButtonAnalysis = true;
    }
    else {
        var submitButtonAnalysis = false;
    }

    switch(action.type) {
        case 'SUBMIT-SV-ANALYSIS':
            return Object.assign({}, state, {
                status: 'default',
                submit_button: {
                    analysis: submitButtonAnalysis
                }
            });
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default page
