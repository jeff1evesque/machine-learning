
## stream-log

  a tiny stream logger.

### Installation

```bash
$ npm install stream-log
```

### Example

![](https://i.cloudup.com/5MIi_cpbL1.png)

```js

var Logger = require('./');
var logger = new Logger(process.stderr);
var types = ['info', 'install', 'fetch', 'fetching'];
var times = 20;

types.forEach(function(type){
  logger.type(type, '36m');
});

logger.type('error', '31;1m', function(){
  logger.end();
  process.exit(1);
});

var i = setInterval(function(){
  var type = types[Math.random() * 4 | 0];
  --times && logger[type]('user/package@1.0.0');
  times || end();
}, 10)

function end(){
  clearInterval(i);
  logger.error(new Error('boom!').stack);
}

```

### License

  (MIT)
