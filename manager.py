'''@manager

This file implements the 'Manager' instance, which allows external scripts to
    be run within the corresponding flask script.  Specifically, 'pytest' is
    used to perform corresponding unit testing.

Note: the 'Manager' instance implements the 'Fask-Script':

    - https://flask-script.readthedocs.io/en/latest/

Note: the 'pytest' instance can be further reviewed:

    - http://docs.pytest.org/en/latest/usage.html

'''

import pytest
from flask.ext.script import Manager

class Manager(object):
    '''@Manager

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(app):
        '''@__init__

        @app, flask app instance, generated from app factory.

        '''

        self.manager = Manager(app)
        self.manager.run(pytest())

    @manager.command
    def pytest():
        '''@pytest
		
        This method implements pytest within the 'test/' directory.

        '''

        pytest.main(['-x', 'test'])
