'''@manager

This file implements the 'Manager' instance, which allows external scripts to
    be run within the corresponding flask script.  Specifically, 'pytest' is
    used to perform corresponding unit testing.

Note: the 'Manager', and 'pytest' instances can further be reviewed:

    - https://flask-script.readthedocs.io/en/latest/
    - http://docs.pytest.org/en/latest/usage.html

'''

import pytest
from factory import create_app
from test.programmatic_interface.pytest_svm_session import *
from flask import Flask

def flask_manager(app):
    class flask_manager(Command):

        manager = Manager(app)

        @pytest.fixture(scope="session")
        def test_app():
            settings_override = {
                settings: {
                    'TESTING': True
                }
            }

            app = create_app(settings_override)

            # Establish an application context before running the tests
            ctx = app.app_context()
            ctx.push()

            # run tests
            check_data_new(ctx)

            def teardown():
                ctx.pop()

            request.addfinalizer(teardown)
            return app
