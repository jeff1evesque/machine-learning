'''@pytest_user_login

This file will test the necessary interfaces required to login.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

from brain.database.retrieve_account import Retrieve_Account
from brain.converter.crypto import verifypass


def test_login(client, live_server):
    '''@test_login

    This method tests the user login process.

    '''

    live_server.start()

    # local variables
    username = 'jeff1evesque'
    password = 'password123'
    authenticate = Retrieve_Account()

    # validate: username exists
    if authenticate.check_username(username)['result']:

        # database query: get hashed password
        hashed_password = authenticate.get_password(username)['result']

        # notification: verify hashed password exists
        if hashed_password:

            # notification: verify password
            assert verifypass(str(password), hashed_password)

        # notification: user does not have a password
        else:
            assert False

    # notification: username does not exist
    else:
        assert False
