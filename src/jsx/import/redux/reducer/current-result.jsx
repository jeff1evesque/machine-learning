/**
 * current-result.jsx: describe data attributes associated with current, or
 *                     latest prediction results.
 *
 * Note: the triple dots is the 'object spread' syntax:
 *
 *       http://redux.js.org/docs/recipes/UsingObjectSpreadOperator.html
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import 'core-js/modules/es6.object.assign';

const result = (state='default', action) => {
    if (action && action.results) {
        var result_type = !!action.results.type ? action.results.type : 'default';
        var result_data = !!action.results.data ? action.results.data : null;

        switch(action.type) {
            case 'SET-CURRENT-RESULT':
                return Object.assign({}, state, {
                    results: {
                        type: result_type,
                        data: result_data
                    }
                });
            default:
                return state;
        }
    }
    return state;
}

// indicate which class can be exported, and instantiated via 'require'
export default result
