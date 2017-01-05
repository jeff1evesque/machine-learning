/**
 * store.jsx: create consistent redux state tree.
 *
 */

import { createStore } from 'redux';
import login from './reducer/login-reducer.jsx';

// redux store: entire state tree for the application
const store = createStore(login);

// manual console trace
store.subscribe(() => {
  console.log('store changed', store.getState())
})

// indicate which class can be exported, and instantiated via 'require'
export default store
