/**
 * valid-int.js: check if provided argument is int type.
 */
function validator(value) {
  return Math.round(parseInt(value)) === parseInt(value);
}

export default function checkValidInt(value) {
  return validator(value);
}