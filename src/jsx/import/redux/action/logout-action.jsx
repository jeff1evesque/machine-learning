/**
 * logout-action.jsx: send logout status from the application to the store.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

function setLogoutState(username) {
    return {
        type: 'logged-out',
        username: username
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setLogoutState
