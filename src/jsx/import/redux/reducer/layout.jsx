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
    if (
        !!action &&
        !!action.layout &&
        !!action.type &&
        action.type === 'SET-LAYOUT'
    ) {
        switch(action.layout) {
            case 'login':
                return Object.assign({}, state, {
                    css : 'container login',
                    type : action.layout,
                });
            case 'register':
                return Object.assign({}, state, {
                    css : 'container register',
                    type : action.layout,
                });
            case 'analysis':
                return Object.assign({}, state, {
                    css : 'container analysis-container',
                    type : action.layout,
                });
            default:
                return state;
        }
    } else {
        return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default layout
