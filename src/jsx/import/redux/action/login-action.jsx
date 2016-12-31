/**
 * login-action.jsx: send login status from the application to the store.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

export function addLogin(value) {
    return { type: 'LOGIN-STATE', value };
}
