'''

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
from logging.handlers import RotatingFileHandler
from flask import Flask
from interface.views import blueprint


# application factory
def create_app(args={'prefix': '', 'settings': ''}):
    # path to hiera
    if args['prefix']:
        prepath = 'hiera/' + args['prefix']
    else:
        prepath = 'hiera'

    # get values from yaml
    with open(prepath + '/database.yaml', 'r') as stream:
        settings = yaml.load(stream)
        sql = settings['database']['mariadb']
        nosql = settings['database']['mongodb']

    with open(prepath + '/common.yaml', 'r') as stream:
        settings = yaml.load(stream)
        general = settings['general']

    with open(prepath + '/webserver.yaml', 'r') as stream:
        settings = yaml.load(stream)
        webserver = settings['webserver']

    with open(prepath + '/cache.yaml', 'r') as stream:
        settings = yaml.load(stream)
        redis = settings['redis']

    with open(prepath + '/application.yaml', 'r') as stream:
        settings = yaml.load(stream)
        application = settings['application']
        crypto = settings['crypto']
        validate_password = settings['validate_password']

    # local variables
    if args['settings']:
        app = Flask(
            __name__,
            args['settings'],
            template_folder='interface/templates',
            static_folder='interface/static',
        )
    else:
        app = Flask(
            __name__,
            template_folder='interface/templates',
            static_folder='interface/static',
        )

    # secret key: used for maintaining flask sessions
    app.secret_key = application['security_key']

    # register blueprint
    app.register_blueprint(blueprint)

    # local logger: used for this module
    root = general['root']
    LOG_PATH = root + webserver['flask']['log_path']
    HANDLER_LEVEL = application['log_level']

    # flask attributes: accessible across application
    app.config.update(
        HOST=general['host'],
        REDIS_HOST=redis['host'],
        REDIS_PORT=redis['port'],
        ROOT=general['root'],
        SQL_HOST=sql['host'],
        SQL_LOG_PATH=sql['log_path'],
        SQL_ML=sql['name'],
        SQL_USERNAME=sql['username'],
        SQL_PASSWORD=sql['password'],
        NOSQL_HOST=nosql['host'],
        NOSQL_DB=nosql['name'],
        NOSQL_USERNAME=nosql['username'],
        NOSQL_PASSWORD=nosql['password'],
        LOG_LEVEL=HANDLER_LEVEL,
        FLASK_LOG_PATH=webserver['flask']['log_path'],
        ERROR_LOG_PATH=application['error_log_path'],
        WARNING_LOG_PATH=application['warning_log_path'],
        INFO_LOG_PATH=application['info_log_path'],
        DEBUG_LOG_PATH=application['debug_log_path'],
        MODEL_TYPE=application['model_type'],
        SALT_LENGTH=crypto['salt_length'],
        SCRYPT_N=crypto['scrypt_n'],
        SCRYPT_R=crypto['scrypt_r'],
        SCRYPT_P=crypto['scrypt_p'],
        PASSWORD_MIN_C=validate_password['password_min_c'],
        PASSWORD_MAX_C=validate_password['password_max_c'],
        USER_ID=0
    )

    # log handler: requires the below logger
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} "
        "%(levelname)s - %(message)s"
    )
    handler = RotatingFileHandler(
        LOG_PATH,
        maxBytes=10000000,
        backupCount=5
    )
    handler.setLevel(HANDLER_LEVEL)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # logger: complements the log handler
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)

    # return
    return app
