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
    switch(action.type) {
        case 'LOGIN':
            return Object.assign({}, state, {
                layout: {
                    css : 'container login',
                    type : action.layout,
                }
            });
        case 'REGISTER':
            return Object.assign({}, state, {
                layout: {
                    css : 'container login',
                    type : action.layout,
                }
            });
        case 'ANALYSIS':
            return Object.assign({}, state, {
                layout: {
                    css : 'container analysis-container',
                    type : action.layout,
                }
            });
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default layout
