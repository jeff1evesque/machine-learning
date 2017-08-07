/**
 * valid-email.js: check if provided argument is a valid email.
 */

function validator(value) {
    var urlregex = new RegExp('^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$');
    return urlregex.test(value);
}

export default function checkValidEmail(value) {
    return validator(value);
}
