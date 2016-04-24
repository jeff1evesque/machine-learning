#!/usr/bin/python

'''@settings

This file contains configuration settings for following:

    - redis
    - database
    - application logging

'''

# variables
ROOT = '/vagrant'

# redis
HOST = 'localhost'
PORT_REDIS = 6379

# application database
DB_USERNAME = 'authenticated'
DB_PASSWORD = 'password'
DB_LOG_PATH = ROOT + '/log/database/'

# application logging: the possible logging levels are constrained by the
#                      python 'logging' module.
#
# @LOG_LEVEL, defines the application baseline (i.e. handler) level for logs.
#     This means the logger level cannot exceed this baseline.
#
#     The following are supported 'LOG_LEVEL' values:
#
#     - ERRORR
#     - WARNING
#     - INFO
#     - DEBUG
#
# Note: the specific log levels can be reviewed:
#
#       https://docs.python.org/2/library/logging.html#logging-levels
#
LOG_LEVEL = 'debug'
ERROR_LOG_PATH = ROOT + '/log/application/error'
WARNING_LOG_PATH = ROOT + '/log/application/warning'
INFO_LOG_PATH = ROOT + '/log/application/info'
DEBUG_LOG_PATH = ROOT + '/log/application/debug'
