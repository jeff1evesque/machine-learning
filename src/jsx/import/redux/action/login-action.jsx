/**
 * login-action.jsx: send login status from the application to the store.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

export function setLoginState(login_state, username) {
    return {
        type: login_state,
        username: value
    };
}
