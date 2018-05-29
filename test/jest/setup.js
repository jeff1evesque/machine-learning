//
// allow the use of 'sessionStorage' within jest + enzyme:
//
//     https://stackoverflow.com/a/47926947
//     https://github.com/jeff1evesque/machine-learning/
//         issues/3087#issuecomment-388694964
//
global.window = {}
import localStorage from 'mock-local-storage'
window.localStorage = global.localStorage

// fail tests for console warnings + errors
console.error = x => { throw x; };
console.warn = x => { throw x; }
