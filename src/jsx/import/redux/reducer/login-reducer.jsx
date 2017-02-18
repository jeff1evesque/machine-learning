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

const user = (state='anonymous', action) => {
    if (action && action.user && !!action.user.name) {
        var username = action.user.name;
    }
    else {
        var username = 'anonymous';
    }

    switch(action.type) {
        case 'LOGGED-IN':
            return Object.assign({}, state, {name : action.user.name});
        case 'LOGGED-OUT':
            return Object.assign({}, state, {name : 'anonymous'});
        default:
            return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default user
