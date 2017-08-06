/**
 * valid-password.js: check if provided argument is a valid password:
 *
 *     - at least one letter
 *     - at least one numeral
 *     - at least 10 overall characters
 */

function validator(value) {
    var urlregex = new RegExp('(?=.{10,}$)(?=.*[A-Za-z])(?=.*[0-9])');
    return urlregex.test(value);
}

export default function checkValidPassword(value) {
    return validator(value);
}
