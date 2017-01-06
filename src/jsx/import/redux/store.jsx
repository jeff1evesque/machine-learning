/**
 * store.jsx: create consistent redux state tree.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
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
