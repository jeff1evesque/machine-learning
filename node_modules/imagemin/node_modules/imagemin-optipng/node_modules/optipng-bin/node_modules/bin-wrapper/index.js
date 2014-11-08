'use strict';

var binCheck = require('bin-check');
var binVersionCheck = require('bin-version-check');
var Download = require('download');
var globby = require('globby');
var isPathGlobal = require('is-path-global');
var path = require('path');
var status = require('download-status');
var symlink = require('lnfs');
var which = require('npm-installed');

/**
 * Initialize a new `BinWrapper`
 *
 * @param {Object} opts
 * @api public
 */

function BinWrapper(opts) {
	if (!(this instanceof BinWrapper)) {
		return new BinWrapper(opts);
	}

	this.env = process.env.PATH.split(path.delimiter);
	this.opts = opts || {};
	this.opts.strip = this.opts.strip <= 0 ? 0 : !this.opts.strip ? 1 : this.opts.strip;
	this.opts.progress = this.opts.progress !== false;
	this._src = [];
}

/**
 * Get or set files to download
 *
 * @param {String} src
 * @param {String} os
 * @param {String} arch
 * @api public
 */

BinWrapper.prototype.src = function (src, os, arch) {
	if (!arguments.length) {
		return this._src;
	}

	this._src.push({
		url: src,
		os: os,
		arch: arch
	});

	return this;
};

/**
 * Get or set the destionation
 *
 * @param {String} dest
 * @api public
 */

BinWrapper.prototype.dest = function (dest) {
	if (!arguments.length) {
		return this._dest;
	}

	this._dest = dest;
	return this;
};

/**
 * Get or set the binary
 *
 * @param {String} bin
 * @api public
 */

BinWrapper.prototype.use = function (bin) {
	if (!arguments.length) {
		return this._use;
	}

	this._use = bin;
	return this;
};

/**
 * Get or set a semver range to test the binary against
 *
 * @param {String} range
 * @api public
 */

BinWrapper.prototype.version = function (range) {
	if (!arguments.length) {
		return this._version;
	}

	this._version = range;
	return this;
};

/**
 * Get the binary path
 *
 * @api public
 */

BinWrapper.prototype.path = function () {
	var dir = path.join(this.dest(), path.dirname(this.use()));
	var bin = path.basename(this.use());

	return path.join(dir, bin);
};

/**
 * Run
 *
 * @param {Array} cmd
 * @param {Function} cb
 * @api public
 */

BinWrapper.prototype.run = function (cmd, cb) {
	var self = this;

	if (typeof cmd === 'function' && !cb) {
		cb = cmd;
		cmd = ['--version'];
	}

	this.search(function (err, file) {
		if (err) {
			cb(err);
			return;
		}

		if (!file) {
			return self.get(function (err) {
				if (err) {
					cb(err);
					return;
				}

				self.test(cmd, cb);
			});
		}

		self.test(cmd, cb);
	});
};

/**
 * Search for the binary
 *
 * @param {Function} cb
 * @api private
 */

BinWrapper.prototype.search = function (cb) {
	var self = this;
	var name = path.basename(this.path());
	var paths = this.path();

	if (this.opts.global) {
		paths = [].concat(paths, this.env.map(function (env) {
			return path.join(env, name);
		}));
	}

	globby(paths, function (err, files) {
		if (err) {
			cb(err);
			return;
		}

		if (self.opts.global) {
			return self.symlink(files, cb);
		}

		cb(null, files[0]);
	});
};

/**
 * Symlink global binary
 *
 * @param {Array} files
 * @param {Function} cb
 * @api private
 */

BinWrapper.prototype.symlink = function (files, cb) {
	var self = this;
	var name = path.basename(this.path());

	files = files.filter(function (file) {
		try {
			return file !== which.sync(name);
		} catch (err) {
			return true;
		}
	});

	if (files.length && isPathGlobal(files[0])) {
		return symlink(files[0], self.path(), function (err) {
			if (err) {
				cb(err);
				return;
			}

			cb(null, files[0]);
		});
	}

	cb(null, files[0]);
};

/**
 * Check if binary is working

 * @param {Array} cmd
 * @param {Function} cb
 * @api private
 */

BinWrapper.prototype.test = function (cmd, cb) {
	var self = this;
	var name = path.basename(this.path());
	var version = this.version();

	if (this.opts.skip) {
		cb();
		return;
	}

	binCheck(this.path(), cmd, function (err, works) {
		if (err) {
			cb(err);
			return;
		}

		if (!works) {
			cb(new Error('The `' + name + '` binary doesn\'t seem to work correctly'));
			return;
		}

		if (version) {
			return binVersionCheck(self.path(), version, cb);
		}

		cb();
	});
};

/**
 * Download files
 *
 * @param {Function} cb
 * @api private
 */

BinWrapper.prototype.get = function (cb) {
	var files = this.parse(this.src());
	var download = new Download({
		extract: true,
		mode: '755',
		strip: this.opts.strip
	});

	files.forEach(function (file) {
		download.get(file.url);
	});

	if (this.opts.progress) {
		download.use(status());
	}

	download.dest(this.dest());
	download.run(cb);
};

/**
 * Parse sources
 *
 * @param {Object} obj
 * @api private
 */

BinWrapper.prototype.parse = function (obj) {
	var arch = process.arch === 'x64' ? 'x64' : process.arch === 'arm' ? 'arm' : 'x86';
	var platform = process.platform;
	var ret = [];

	obj.filter(function (o) {
		if (o.os && o.os === platform && o.arch && o.arch === arch) {
			return ret.push(o);
		} else if (o.os && o.os === platform && !o.arch) {
			return ret.push(o);
		} else if (!o.os && !o.arch) {
			return ret.push(o);
		}
	});

	return ret;
};

/**
 * Module exports
 */

module.exports = BinWrapper;
