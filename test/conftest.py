'''@manager

This file creates the necessary constructs, which pytest will load, and make
    for each available for each pytest instance.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

import pytest
import sys
sys.path.append("..")
from factory import create_app

@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app
