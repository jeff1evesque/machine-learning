'''@manager

This file implements the 'Manager' instance, which allows external scripts to
    be run within the corresponding flask script.  Specifically, 'pytest' is
    used to perform corresponding unit testing.

Note: the 'Manager', and 'pytest' instances can further be reviewed:

    - https://flask-script.readthedocs.io/en/latest/
    - http://docs.pytest.org/en/latest/usage.html

'''

import pytest
import sys
sys.path.append("..")
from factory import create_app
#from test.programmatic_interface.pytest_svm_session import *
from flask import Flask, url_for


@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app
