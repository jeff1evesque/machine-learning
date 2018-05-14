// https://stackoverflow.com/a/47926947
mock-local-storage

// fail tests for console warnings + errors
console.error = x => { throw x; };
console.warn = x => { throw x; }
