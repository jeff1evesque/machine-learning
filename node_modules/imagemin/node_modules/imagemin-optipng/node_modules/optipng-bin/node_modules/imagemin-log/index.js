'use strict';

var Log = require('stream-log');

/**
 * Initialize `Log`
 */

var log = new Log(process.stderr, 2)
	.type('info', '36m')
	.type('warn', '33m');

/**
 * Success
 */

log.type('success', '32m', function () {
	log.end();
});

/**
 * Error
 */

log.type('error', '31m', function () {
	log.end();
});

/**
 * Module exports
 */

module.exports = log;
