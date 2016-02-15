/**
 * valid_file.js: check if provided argument has proper file extension.
 */
function validator(value) {
  var validExtensions = ['csv', 'xml', 'json'];
  if ($.inArray(value.split('.').pop().toLowerCase(), validExtensions) >= 0) {
    return true;
  } else {
    return false;
  }
}

export function checkValidFile(value) {
  return validator(value);
}