/**
 * login.jsx: describe how login state changes.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

function login(state='logged-out', action) {
    switch(action.type) {
        case 'LOGIN':
            return 'logged-in';
        case 'LOGOUT':
            return 'logged-out';
    default:
        return state;
    }
}
