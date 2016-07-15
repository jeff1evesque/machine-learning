'''@manager

This file implements the 'Manager' instance, which allows external scripts to
    be run within the corresponding flask script.  Specifically, 'pytest' is
    used to perform corresponding unit testing.

Note: the 'Manager', and 'pytest' instances can further be reviewed:

    - https://flask-script.readthedocs.io/en/latest/
    - http://docs.pytest.org/en/latest/usage.html

'''

import pytest
from flask.ext.script import Manager, Command

def flask_manager(app, prefix):
    class flask_manager(Command):

        manager = Manager(app)

        @manager.command
        def run():
            pytest.main(['-x', 'test'])

        manager.add_command('test', run())