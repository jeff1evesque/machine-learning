'''@factory

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
from flask import Flask
from interface.views import blueprint


# application factory
def create_app(args={'prefix': '', 'settings': ''}):

    # path to hiera
    if args['prefix']:
        path = 'hiera/' + args['prefix'] + '/hiera/settings.yaml'
    else:
        path = 'hiera/settings.yaml'

    try:
        # define configuration
        with open(path, 'r') as stream:
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
            settings = yaml.load(stream)

            # secret key: used for maintaining flask sessions
            app.secret_key = settings['application']['security_key']

            # register blueprint
            app.register_blueprint(blueprint)

            # local logger: used for this module
            root = settings['general']['root']
            LOG_PATH = root + settings['webserver']['flask_log_path']
            HANDLER_LEVEL = settings['application']['log_level']

            # flask attributes: accessible across application
            app.config.update(
                HOST=settings['general']['host'],
                REDIS_HOST=settings['redis']['host'],
                REDIS_PORT=settings['redis']['port'],
                ROOT=settings['general']['root'],
                DB_HOST=settings['database']['host'],
                DB_LOG_PATH=settings['database']['log_path'],
                DB_ML=settings['database']['name'],
                DB_USERNAME=settings['database']['username'],
                DB_PASSWORD=settings['database']['password'],
                LOG_LEVEL=HANDLER_LEVEL,
                FLASK_LOG_PATH=settings['webserver']['flask']['log_path'],
                ERROR_LOG_PATH=settings['application']['error_log_path'],
                WARNING_LOG_PATH=settings['application']['warning_log_path'],
                INFO_LOG_PATH=settings['application']['info_log_path'],
                DEBUG_LOG_PATH=settings['application']['debug_log_path'],
                MODEL_TYPE=settings['application']['model_type'],
                SALT_LENGTH=settings['crypto']['salt_length'],
                SCRYPT_N=settings['crypto']['scrypt_n'],
                SCRYPT_R=settings['crypto']['scrypt_r'],
                SCRYPT_P=settings['crypto']['scrypt_p'],
                PASSWORD_MIN_C=settings['validate_password']['password_min_c'],
                PASSWORD_MAX_C=settings['validate_password']['password_max_c'],
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

    except Exception as error:
        print error
