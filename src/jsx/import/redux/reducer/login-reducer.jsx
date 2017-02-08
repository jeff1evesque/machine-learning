/**
 * login-reducer.jsx: describe how login state changes.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

const storageMiddleware = store => next => action => {
    if (action.type === 'LOGGED-IN') {
        sessionStorage.setItem('username', action.username);
    } else if (action.type === 'LOGGED-OUT') {
        sessionStorage.removeItem('username');
    }
    return next(action);
}

// indicate which class can be exported, and instantiated via 'require'
export default storageMiddleware
