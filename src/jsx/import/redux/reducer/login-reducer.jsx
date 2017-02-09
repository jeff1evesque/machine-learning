/**
 * login-reducer.jsx: describe how login state changes.
 *
 * Note: the triple dots is the 'object spread' syntax:
 *
 *       http://redux.js.org/docs/recipes/UsingObjectSpreadOperator.html
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

const login = (state='anonymous', action) => {
    switch(action.type) {
        case 'LOGGED-IN':
            return Object.assign({}, state, { user : action.username});
        case 'LOGGED-OUT':
            return Object.assign({}, state, { user : action.username});
    default:
        return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default login
