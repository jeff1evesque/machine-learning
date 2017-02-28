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
    switch(action.type) {
        case 'SET-RESULTS':
            return Object.assign({}, state, {
                type: !!action.results.type ? action.results.type : 'default',
                data: !!action.results.data ? action.results.data : null
            });
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default data
