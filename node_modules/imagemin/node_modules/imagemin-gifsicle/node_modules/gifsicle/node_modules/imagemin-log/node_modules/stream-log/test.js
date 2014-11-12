
var assert = require('better-assert');
var Writable = require('stream').Writable;
var Logger = require('./');

describe('Logger(stream)', function(){
  var logger, stream;

  beforeEach(function(){
    stream = new Writable;
    stream._write = function(chunk, enc, fn){
      (this.data = this.data || []).push(chunk);
      fn();
    };
    logger = new Logger(stream);
  });

  it('should not require new', function(){
    var logger = Logger(stream);
    assert(logger instanceof Logger);
  });

  describe('#type(name)', function () {
    it('should default to 30m', function(){
      logger.type('foo');
      logger.foo('bar');
      assert('\n   \u001b[30mfoo\u001b[m : bar\n' == stream.data.join(''));
    });

    it('should support #type("wrote")', function(){
      logger.type('wrote');
      logger.wrote('foo');
      assert('\n   \u001b[30mwrote\u001b[m : foo\n' == stream.data.join(''));
    })

    it('should add a trailing newline', function(){
      logger.type('foo');
      logger.foo('bar');
      logger.foo('qux');
      var expected = [
        '',
        '   \u001b[30mfoo\u001b[m : bar',
        '   \u001b[30mfoo\u001b[m : qux',
        ''
      ].join('\n');
      assert(expected == stream.data.join(''));
    });
  });

  describe('#type(name, color)', function(){
    it('should add a "type" method', function(){
      assert('function' != typeof logger.foo);
      logger.type('foo', '36m');
      assert('function' == typeof logger.foo);
    });

    it('should add \\n on first write', function() {
      logger.type('foo', '36m');
      logger.foo('bar');
      assert('\n' == stream.data[0]);
    });

    it('should wrap "name" in color', function(){
      logger.type('foo', '36m');
      logger.foo('bar');
      var str = stream.data.join('').toString();
      assert('\n   \u001b[36mfoo\u001b[m : bar\n' == str);
    });

    it('should format variadic arguments', function(){
      logger.type('foo', '36m');
      logger.foo('bar %s', 'baz');
      var str = stream.data.join('').toString();
      assert('\n   \u001b[36mfoo\u001b[m : bar baz\n' == str);
    });
  });

  describe('#type(name, color, fn)', function(){
    it('should add a "type" method and invoke fn', function(){
      var invoked = false;
      logger.type('foo', '36m', function(){
        invoked = true;
      });
      logger.foo('bar');
      assert(invoked);
    });
  });

  describe('#end()', function(){
    it('should print \\n\\n', function() {
      logger.type('foo', '36m');
      logger.foo('bar');
      stream.data = [];
      logger.end();
      assert('\n\n' == stream.data[0]);
    });
  });
});
