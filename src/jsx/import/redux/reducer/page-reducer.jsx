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

const page = (state, action) => {
    if (!!action && !!action.page && !!action.page.layout) {
        return Object.assign({}, state, {
            page: {
                layout: action.page.layout
            }
        });
    }
    else {
        return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default page
