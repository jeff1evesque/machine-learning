/**
 * valid_string.js: check if provided argument is string type.
 */
function validator(value) {
  if (typeof(value) === 'string') {
    return true;
  } else {
    return false;
  }
}

export function checkValidString(value) {
  return validator(value);
}