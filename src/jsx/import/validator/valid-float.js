/**
 * valid-float.js: check if provided argument is float type.
 */

function validator(value) {
  // convert to string
    if (typeof value != 'string') {
        value = value.toString();
    }

    if (value.match(/^-0*.0*$/)) {
      // invalid condition: -0, and -0.0
        return false;
    } else if (value.match(/^-?(0|[1-9][0-9]*)(e[+|-][1-9]*[0-9]*)$/)) {
      // validate integers: cannot start with 0 (except trivial 0)
        return true;
    } else if (value.match(/^-?(0|[1-9][0-9]*)?\.?([1-9]*[0-9]+)(e[+|-][1-9]*[0-9]*)?$/)) {
      // validate floats: cannot start with 0 (except trivial 0.x)
        return true;
    } else {
      // invalid condition: general
        return false;
    }
}

export default function checkValidFloat(value) {
    return validator(value);
}
