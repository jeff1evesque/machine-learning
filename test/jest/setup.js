// fail tests for console warnings + errors
console.error = x => { throw x; };
console.warn = x => { throw x; }
