/**
 * login-reducer.jsx: describe how login state changes.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

const login = (state='logged-out', action) => {
    switch(action.type) {
        case 'LOGIN':
            return 'logged-in';
        case 'LOGOUT':
            return 'logged-out';
    default:
        return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default login
