/**
 * layout.jsx: describe the overall page layout.
 *
 * Note: the triple dots is the 'object spread' syntax:
 *
 *       http://redux.js.org/docs/recipes/UsingObjectSpreadOperator.html
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import 'core-js/modules/es6.object.assign';

const layout = (state='analysis', action) => {
    if (action && action.user && !!action.user.name) {
        var username = action.user.name;
    }
    else {
        var username = 'anonymous';
    }

    switch(action.layout) {
        case 'LOGIN':
            return Object.assign({}, state, {
                css : 'container login',
                layout : action.layout,
            });
        case 'REGISTER':
            return Object.assign({}, state, {
                css : 'container login',
                layout : action.register,
            });
        case 'ANALYSIS':
            return Object.assign({}, state, {
                css : 'container analysis-container',
                layout : action.register,
            });
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default layout
