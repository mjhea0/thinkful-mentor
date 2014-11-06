#!/usr/bin/env node

/**
 * Now use CoffeeScript.
 */
require('coffee-script');

/**
 * Importing local modules.
 */
var program = require('./program');
var processor = require('./processor');
var utils = require('./utils');

if (require.main === module ) {
	// Parses and processes command line arguments.
	program.parse(process.argv);
	processor.process(program);
} else { // Library mode.
    module.exports.verify = utils.verify;
    module.exports.isCryptInstalled = utils.isCryptInstalled;
}