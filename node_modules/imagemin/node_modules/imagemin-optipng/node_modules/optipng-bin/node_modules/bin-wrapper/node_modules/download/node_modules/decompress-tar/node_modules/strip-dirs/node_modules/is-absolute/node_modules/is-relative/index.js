/**
 * is-relative <https://github.com/jonschlinkert/is-relative>
 *
 * Copyright (c) 2014 Jon Schlinkert, contributors.
 * Licensed under the MIT license.
 */

'use strict';

/**
 * **Example**:
 *
 * ```js
 * var isRelative = require('is-relative');
 * isRelative('test/fixtures/docs/new/file.txt');
 * //=> true
 * ```
 *
 * @param {String} `filepath` Path to test.
 * @return {Boolean}
 */

module.exports = function isRelative(filepath) {
  if (typeof filepath !== 'string') {
    throw new Error('isRelative expects a string.');
  }
  return !/^([a-z]+:)?[\\\/]/i.test(filepath);
};