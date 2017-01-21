/**
 * valid-file.js: check if provided argument has proper file extension.
 */
function validator(value) {
  var validExtensions = ['csv', 'xml', 'json'];
  if (validExtensions.indexOf(value.split('.').pop().toLowerCase()) > -1) {
    return true;
  } else {
    return false;
  }
}

export default function checkValidFile(value) {
  return validator(value);
}