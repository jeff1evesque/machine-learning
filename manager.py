'''@manager

This file implements the 'Manager' instance, which allows external scripts to
    be run within the corresponding flask script.  Specifically, 'pytest' is
    used to perform corresponding unit testing.

Note: the 'Manager', and 'pytest' instances can further be reviewed:

    - https://flask-script.readthedocs.io/en/latest/
    - http://docs.pytest.org/en/latest/usage.html

'''

import pytest
from flask.ext.script import Manager

class Manager(object):
    '''@Manager

    This constructor is responsible for defining class variables.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(app):
        '''@__init__

        This constructor is responsible for defining class variables.

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
