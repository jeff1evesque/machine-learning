/**
 * valid_string.js: check if provided argument is string type.
 */
function validator(value) {
  return typeof value === 'string';
}

export function checkValidString(value) {
  return validator(value);
}