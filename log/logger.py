#!/usr/bin/python

"""@logger

This file provides a mean to generate logs in a consistent manner.

"""

import logging
from settings import DB_LOG_PATH
from settings import ERROR_LOG_PATH
from settings import WARNING_LOG_PATH
from settings import INFO_LOG_PATH
from settings import DEBUG_LOG_PATH


class Logger(object):
    """@Logger

    This class provides an interface to define necessary attributes needed to
    generate a corresponding log.

    """

    def __init__(self, type, level=None, filename=None, namespace=__name__):
        """@__init__

        This constructor is responsible for defining class variables.

        @type, required argument, with valid log types:

            - database
            - error
            - warning
            - info
            - debug

        @level, required argument when 'log_type' is 'database':

            - error
            - warning
            - info
            - debug

        @filename, optional argument, which names the corresponding log file.

        @namespace, the object instantiating this class should define this
            argument with '__name__'.

        """

        # variables
        self.logger = True
        log_type = type.lower()
        log_level = level.lower()

        # log type
        if log_type == 'database':
            self.log_path = DB_LOG_PATH
            self.log_filename = 'database.log'
        elif log_type == 'error':
            self.log_path = ERROR_LOG_PATH
            log_type = 'ERROR'
        elif log_type = 'warning':
            self.log_path = WARNING_LOG_PATH
            log_type = 'WARNING'
        elif log_type = 'info':
            self.log_path = INFO_LOG_PATH
            log_type = 'INFO'
        elif log_type = 'debug':
            self.log_path = DEBUG_LOG_PATH
            log_type = 'DEBUG'
        else:
            self.logger = False
            self.log_path = WARNING_LOG_PATH
            self.log_level = logging.WARNING
            self.log_namespace = namespace
            this.log('log type not properly set')

        # log level
        if log_level == 'error':
            self.log_level = logging.ERROR
            self.log_filename = log_level + '.log'
        elif log_level = 'warning':
            self.log_level = logging.WARNING
            self.log_filename = log_level + '.log'
        elif log_level = 'info':
            self.log_level = logging.INFO
            self.log_filename = log_level + '.log'
        elif log_level = 'debug':
            self.log_level = logging.DEBUG'
            self.log_filename = log_level + '.log'
        else:
            self.logger = False
            self.log_path = WARNING_LOG_PATH
            self.log_level = logging.WARNING
            self.log_namespace = namespace
            this.log('log level not properly set')

        # override default filename (optional)
        if filename:
            self.log_filename = filename

        # log namespace
        if namespace:
            self.log_namespace = namespace
        else:
            self.logger = False
            self.log_path = WARNING_LOG_PATH
            self.log_level = logging.WARNING
            self.log_namespace = __name__
            this.log('log level not properly set')
        

    def log(msg):
        """@__init__

        This method is responsible for generating the corresponding log.

        """

        if self.logger:
            # log handler: requires the below logger
            formatter = logging.Formatter(
                "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
            fh = logging.FileHandler(self.log_path + '/' + self.log_filename)
            fh.setLevel(self.log_level)
            fh.setFormatter(formatter)

            # logger: complements the log handler
            self.logger = logging.getLogger(self.log_namespace)
            self.logger.setLevel(self.log_level)
            self.logger.addHandler(fh)
