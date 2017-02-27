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
        var type = !!action.type ? action.type : 'default';
        var data = !!action.data ? action.data : null;
    }

    switch(action.type) {
        case 'SET-RESULTS':
            return Object.assign({}, state, {
                type: 'default',
                data: data
            });
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default data
