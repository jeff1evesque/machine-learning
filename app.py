'''@app

This file is the acting web server.

@debug, enables debugging, and tracebacks
@host, tells the OS (guest VM) to accept connections from all public IP
    addresses.

Note: both the handler, and logger has levels. If the level of the logger is
      higher than that of the handler, no messages will be handled by the
      corresponding handler.

'''

import yaml
import logging
from log.logger import Logger
from logging.handlers import RotatingFileHandler
from interface import app

# get configuration
with open('settings.yml', 'r') as stream:
    try:
        settings = yaml.load(stream)
        root = settings['general']['root']
        LOG_PATH = root + '/' + settings['server']['flask_log_path']
        HANDLER_LEVEL = settings['application']['log_level']
    except yaml.YAMLError as error:
        self.logger = Logger('error', 'yaml')
        self.logger.log(error)

# log handler: requires the below logger
formatter = logging.Formatter(
    "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler(LOG_PATH, maxBytes=10000000, backupCount=5)
handler.setLevel(HANDLER_LEVEL)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

# logger: complements the log handler
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)
log.addHandler(handler)

# run application
app.run(host='0.0.0.0')
