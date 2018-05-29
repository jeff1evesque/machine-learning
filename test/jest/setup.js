//
// allow the use of 'sessionStorage' within jest + enzyme:
//
//     https://stackoverflow.com/a/47926947
//     https://stackoverflow.com/a/32911774
//     https://github.com/jeff1evesque/machine-learning/
//         issues/3087#issuecomment-388694964
//
var localStorageMock = (function() {
  var store = {};
  return {
    getItem: function(key) {
      return store[key];
    },
    setItem: function(key, value) {
      store[key] = value.toString();
    },
    clear: function() {
      store = {};
    },
    removeItem: function(key) {
      delete store[key];
    }
  };
})();
Object.defineProperty(window, 'localStorage', { value: localStorageMock });

// fail tests for console warnings + errors
console.error = x => { throw x; };
console.warn = x => { throw x; }
