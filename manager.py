'''@manager

This file implements 'Manager' instance, which allows external scripts to be
    run within the corresponding flask script.

Note: the 'Manager' instance implements the 'Fask-Script':

    - https://flask-script.readthedocs.io/en/latest/

'''

import pytest
from flask.ext.script import Manager

class Manager(object):
    '''@Manager

    This class provides an interface to 'Manager' instance.

    @app, 

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(app):

        self.manager = Manager(app)
        self.manager.run(pytest())

    @manager.command
    def pytest():
        pytest.main(['-x', 'test'])
