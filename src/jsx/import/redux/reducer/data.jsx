/**
 * data.jsx: describe data attributes associated with predictions.
 *
 * Note: the triple dots is the 'object spread' syntax:
 *
 *       http://redux.js.org/docs/recipes/UsingObjectSpreadOperator.html
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import 'core-js/modules/es6.object.assign';

const data = (state='default', action) => {
    var type = 'default';
    var data = null;

    if (
        action &&
        action.results
    ) {
        var result_type = !!action.results.type ? action.results.type : 'default';
        var result_data = !!action.results.data ? action.results.data : null;
    }

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

// indicate which class can be exported, and instantiated via 'require'
export default data
