/**
 * login.jsx: send login status to the redux store.
 *
 */

function setLoginState(username) {
    return {
        type: 'LOGGED-IN',
        user: {
            name: username
        }
    };
}

// indicate which class can be exported, and instantiated via 'require'
export default setLoginState
