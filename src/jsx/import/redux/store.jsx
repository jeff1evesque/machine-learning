/**
 * store.jsx: create consistent redux state tree.
 *
 * Note: importing 'named export' (multiple export statements in a module),
 *       requires the object being imported, to be surrounded by { brackets }.
 *
 * Note: when debugging in this script, either implement 'middleware', or add
 *       the following after the 'store' definition:
 *
 *       // manual console trace
 *         store.subscribe(() => {
 *             console.log('store changed', store.getState());
 *         })
 *
 */

import { createStore, combineReducers } from 'redux';
import user from './reducer/login.jsx';
import page from './reducer/page.jsx';

// username from sessionStorage
const username = sessionStorage.getItem('username') || 'anonymous'

// create and initialize redux
const store = createStore(combineReducers({user, page}), {
    user: {name: username},
    page: {
        status: 'default',
        button: {
            submit_analysis: false,
            goto_results: false
        }
    }
});

// indicate which class can be exported, and instantiated via 'require'
export default store
