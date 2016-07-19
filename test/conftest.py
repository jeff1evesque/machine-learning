'''@manager

This file creates the necessary constructs, which pytest will load, and make
    available for each pytest execution instance.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

import pytest
import sys
sys.path.append('..')
from factory import create_app # noqa


@pytest.fixture
def app():
    app = create_app()
    app.testing = True
    return app
