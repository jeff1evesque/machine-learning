/**
 * login-reducer.jsx: describe how login state changes.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

const login = (state='anonymous', action) => {
    switch(action.type) {
        case 'LOGGED-IN':
            return action.username;
        case 'LOGGED-OUT':
            return 'anonymous';
    default:
        return state;
    }
}

// indicate which class can be exported, and instantiated via 'require'
export default login
