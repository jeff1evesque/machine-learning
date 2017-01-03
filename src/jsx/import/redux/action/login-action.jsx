/**
 * login-action.jsx: send login status from the application to the store.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

function setLoginState(login_state, username) {
    return {
        type: login_state,
        username: value
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setLoginState
