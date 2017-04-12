'''

This file will test the necessary interfaces required to login.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

from flask import session
from brain.database.retrieve_account import Retrieve_Account
from brain.converter.crypto import verify_pass


def test_login(client, live_server):
    '''

    This method tests the user login process. Specifically, the tests include
    verifying the user credentials (i.e. username, and password). Then, it
    checks, if the flask session has successfully stored the userid (i.e. uid),
    into flask's session implementation.

    '''

    live_server.start()

    # local variables
    username = 'jeff1evesque'
    password = 'password123'
    url = '/login'
    authenticate = Retrieve_Account()

    # validate: username exists
    if authenticate.check_username(username)['result']:

        # database query: get hashed password
        hashed_password = authenticate.get_password(username)['result']

        # notification: verify hashed password exists
        if hashed_password:

            # notification: verify password
            if verify_pass(str(password), hashed_password):
                # post requests: login response
                payload = {'user[login]': username, 'user[password]': password}
                login = client.post(url, data=payload)

                assert login.status_code == 200
                assert session.get('uid') == 1
            else:
                assert False

        # notification: user does not have a password
        else:
            assert False

    # notification: username does not exist
    else:
        assert False
