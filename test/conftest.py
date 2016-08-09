'''@conftest

This file creates the necessary constructs, which pytest will load, and make
    available for each pytest execution instance.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

import pytest
import sys
sys.path.append('..')
from factory import create_app  # noqa


@pytest.fixture
def app(report):
    try:
        args = {
            'prefix': 'test',
            'settings': ''
        }
        app = create_app(args)
        app.testing = True

        # pytest exception: collection error
        if report.failed:
            raise pytest.UsageError('Errors during collection, aborting')

        return app

    # general exception
    except Exception as error:
        raise pytest.UsageError(error)
