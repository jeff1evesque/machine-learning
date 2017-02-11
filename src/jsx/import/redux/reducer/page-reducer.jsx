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

const pageConfig = (state, action) => {
    switch(action.type) {
        case 'PAGE-CONFIG':
            return Object.assign({}, state, {
                page: {
                    layout: action.page.layout
                }
            });
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default pageConfig
