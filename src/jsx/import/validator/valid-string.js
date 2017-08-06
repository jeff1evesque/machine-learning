/**
 * valid-string.js: check if provided argument is string type.
 */

function validator(value) {
    if (typeof value === 'string' && value.length > 0) {
        return true;
    }
    else {
        return false;
    }
}

export default function checkValidString(value) {
    return validator(value);
}
