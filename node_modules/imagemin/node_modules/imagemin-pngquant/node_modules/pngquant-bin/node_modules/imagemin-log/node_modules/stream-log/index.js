
/**
 * Module dependencies.
 */

var longest = require('longest');
var fmt = require('util').format;
var assert = require('assert');

/**
 * Expose `Logger`
 */

module.exports = Logger;

/**
 * Initialize `Logger`
 *
 * @param {Stream} stream
 * @param {Number} indent
 * @api public
 */

function Logger(stream, indent){
  if (!(this instanceof Logger)) return new Logger(stream, indent);
  this.stream = stream;
  this.types = [];
  this.indent = indent || 3;
}

/**
 * Add `type` with `color`.
 *
 * Example:
 *
 *    logger.type('log', '36m');
 *    logger.log('woot %d', 9);
 *
 *    logger.type('error', '36m', function(){
 *      logger.end();
 *      process.exit(1);
 *    });
 *
 *    logger.error('%s', err.stack);
 *
 * @param {String} type
 * @param {String} color
 * @param {Function} fn
 * @return {Logger}
 * @api private
 */

Logger.prototype.type = function(type, color, fn){
  assert(!this[type], '.' + type + '() already exists');
  var color = color || '30m';
  var self = this;
  this.types.push(type);
  this[type] = function(){
    var args = [].slice.call(arguments);
    self.__log__(type, color, args);
    fn && fn();
  };
  return this;
};

/**
 * Log `type`, `color` with `args`.
 *
 * @param {String} type
 * @param {String} color
 * @param {Function} fn
 * @api private
 */

Logger.prototype.__log__ = function(type, color, args){
  if (!this._wrote) {
    this.stream.write('\n');
    this._wrote = true;
  }
  var pad = this.padleft(type);
  var msg = '%s\033[%s%s\033[m';
  if (args.length) msg += ' : ';
  msg = fmt(msg, pad, color, type);
  if (args.length) msg += fmt.apply(null, args);
  this.stream.write(msg + '\n');
  return this;
};

/**
 * Pad `type` left.
 *
 * @param {String} type
 * @return {String}
 * @api private
 */

Logger.prototype.padleft = function(type){
  var len = longest(this.types).length;
  return Array(this.indent + 1 + len - type.length).join(' ');
};

/**
 * End.
 *
 * @api public
 */

Logger.prototype.end = function(){
  this.stream.write('\n\n');
  return this;
};
