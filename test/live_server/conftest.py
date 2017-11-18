'''

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
def app():
    try:
        args = {
            'prefix': 'test/hiera',
            'instance': 'api'
        }
        app = create_app(args)
        app.testing = True

        return app

    except:
        raise


@pytest.fixture
def token(client):
    '''

    This method will login, and return the corresponding token.

    '''

    # local variables
    username = 'jeff1evesque'
    password = 'password123'
    payload = {'user[login]': username, 'user[password]': password}

    # login and get flask-jwt token
    login = client.post(
        '/login',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(payload)
    )
    return login.json['access_token']
