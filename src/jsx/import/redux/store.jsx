/**
 * login-action.jsx: send login status from the application to the store.
 *
 * Note: this script implements jsx (reactjs) syntax.
 *
 */

import { createStore } from 'redux';

// redux store: entire state tree for the application
const store = createStore(login);

// manual console trace
store.subscribe(() => {
  console.log('store changed', store.getState())
})

// indicate which class can be exported, and instantiated via 'require'
export default store
