/**
 * login-action.jsx: send login status from the application to the store.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

function setLoginState(username) {
    return {
        type: 'LOGGED-IN',
        username: username
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setLoginState
