/**
 * login-action.jsx: send login status to the redux store.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

function setLoginState(username) {
    return {
        type: 'LOGGED-IN',
        name: username
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setLoginState
