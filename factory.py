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
from flask import Flask, g
from brain.cache.session import RedisSessionInterface
from extensions import jwt_manager
from logging.handlers import RotatingFileHandler
from interface.views import blueprint


# application factory
def create_app(args={'prefix': '', 'instance': 'web'}):
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
        cache = settings['redis']

    with open(prepath + '/application.yaml', 'r') as stream:
        settings = yaml.load(stream)
        application = settings['application']
        crypto = settings['crypto']
        validate_password = settings['validate_password']

    # local variables
    app = Flask(
        __name__,
        template_folder='interface/templates',
        static_folder='interface/static',
    )

    # flask 'session' secret key
    app.secret_key = application['security_key']

    # set the flask-jwt-extended extension
    if args['instance'] == 'api':
        app.config['JWT_SECRET_KEY'] = application['security_key']
        app.config['PROPAGATE_EXCEPTIONS'] = False
        jwt_manager.init_app(app)

    # replace default cookie session with server-side redis
    else:
        app.session_interface = RedisSessionInterface(
            cache['host'],
            cache['port'],
            cache['db']
        )

    # register blueprint
    app.register_blueprint(blueprint)

    # local logger: used for this module
    ROOT = general['root']
    LOG_PATH = ROOT + webserver['flask']['log_path']
    HANDLER_LEVEL = application['log_level']

    # flask attributes: accessible across application
    app.config.update(
        HOST=general['host'],
        CACHE_HOST=cache['host'],
        CACHE_PORT=cache['port'],
        CACHE_DB=cache['db'],
        ROOT=ROOT,
        SQL_HOST=sql['host'],
        SQL_LOG_PATH=sql['log_path'],
        SQL_DB=sql['name'],
        SQL_USERNAME=sql['username'],
        SQL_PASSWORD=sql['password'],
        NOSQL_HOST=nosql['hostname'] + ':' + str(nosql['net']['port']),
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
        MAXCOL_ANON=application['dataset']['anonymous']['max_collection'],
        MAXDOC_ANON=application['dataset']['anonymous']['max_document'],
        MAXCOL_AUTH=application['dataset']['authenticated']['max_collection'],
        MAXDOC_AUTH=application['dataset']['authenticated']['max_document'],
        SALT_LENGTH=crypto['salt_length'],
        SCRYPT_N=crypto['scrypt_n'],
        SCRYPT_R=crypto['scrypt_r'],
        SCRYPT_P=crypto['scrypt_p'],
        PASSWORD_MIN_C=validate_password['password_min_c'],
        PASSWORD_MAX_C=validate_password['password_max_c'],
        USER_ID=0
    )

    # log format
    formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} "
        "%(levelname)s - %(message)s"
    )

    # initialize the log handler
    handler = RotatingFileHandler(
        LOG_PATH,
        maxBytes=10000000,
        backupCount=5
    )

    # log handler level
    handler.setLevel(HANDLER_LEVEL)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

    # app logger level
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)

    # return
    return app


def register_teardowns(app):
    @app.teardown_appcontext
    def close_db(error):
        '''

        This function closes the database connection, everytime the app context
        tears down. A teardown can happen because of two reasons: either
        everything went well (the error parameter will be None) or an exception
        happened, in which case the error is passed to the teardown function.

        Note: http://flask.pocoo.org/docs/0.12/tutorial/dbcon/

        '''

        if hasattr(g, 'mongodb'):
            g.mongodb.close()

        if hasattr(g, 'mariadb'):
            g.mariadb.close()
