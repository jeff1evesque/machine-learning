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

export function checkValidInt(value) {
  return validator(value);
}