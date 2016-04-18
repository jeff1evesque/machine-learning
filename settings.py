#!/usr/bin/python

'''@settings

This file contains sensitive configuration settings used to implement redis,
and to establish required database connection(s).

'''

## server configuration
ROOT = '/vagrant'
HOST = 'localhost'
PORT_REDIS = 6379

## application database
DB_USERNAME = 'authenticated'
DB_PASSWORD = 'password'
DB_LOG_PATH = ROOT + '/log/database/'

## logging: the possible log levels are constrained by -
##
## https://docs.python.org/2/library/logging.html#logging-levels
LOG_LEVEL        = 'debug'
ERROR_LOG_PATH   = ROOT + '/log/error'
WARNING_LOG_PATH = ROOT + '/log/warning'
INFO_LOG_PATH    = ROOT + '/log/info'
DEBUG_LOG_PATH   = ROOT + '/log/debug'