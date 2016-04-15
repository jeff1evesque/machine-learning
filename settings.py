#!/usr/bin/python

'''@settings

This file contains sensitive configuration settings used to implement redis,
and to establish required database connection(s).

'''

ROOT = '/vagrant'
HOST = 'localhost'
PORT_REDIS = 6379

DB_USERNAME = 'authenticated'
DB_PASSWORD = 'password'
DB_LOG_PATH = ROOT + '/log/database.log'

ERROR_LOG_PATH   = ROOT + '/log/error.log'
WARNING_LOG_PATH = ROOT + '/log/warning.log'
INFO_LOG_PATH    = ROOT + '/log/info.log'
DEBUG_LOG_PATH   = ROOT + '/log/debug.log'