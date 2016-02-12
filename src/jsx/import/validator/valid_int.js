/**
 * valid_int.js: check if provided argument is int type.
 */
function validator(value) {
  if (Math.round(parseInt(value)) === parseInt(value)) {
    return true;
  } else {
    return false;
  }
}

export function checkValidInt(value) {
  return validator(value);
}