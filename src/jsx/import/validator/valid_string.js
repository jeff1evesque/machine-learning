/**
 * valid_string.js: check if provided argument is string type.
 */
function validator(value) {
  return typeof value === 'string';
}

export default function checkValidInt(value) {
  return validator(value);
}