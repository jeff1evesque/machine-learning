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
    var result_keys = false;
    var result_values = false;

    if (
        action &&
        action.results
    ) {
        var type = !!action.type ? action.type ? 'default';
        var result_keys = !!action.results.keys ? action.results.keys : null;
        var result_values = !!action.results.values ? action.results.values : null;
    }

    switch(action.type) {
        case 'DISPLAY-RESULTS':
            return Object.assign({}, state, {
                type: 'default',
                results: {
                    keys: result_keys,
                    values: result_values
                }
            });
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default data
