'''@pytest_account_login

This file will test the necessary interfaces required to login.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

from brain.validator.validate_password import validate_password
from brain.database.retrieve_account import Retrieve_Account
from brain.converter.crypto import hashpass, verifypass


def test_login(client, live_server):
    '''@test_login

    This method tests the user registration process.

    '''

    live_server.start()

    # local variables
    username = 'jeff1evesque'
    password = 'password123'
    authenticate = Retrieve_Account()

    # validate: check username exists
    if authenticate.check_username(username)['result']:

        # database query: get hashed password
        hashed_password = authenticate.get_password(user)

        # notification: verify hashed password exists
        if hashed_password:

            # notification: verify password
            assert verifypass(password, hashed_password)

        # notification: user does not have password
        else:
            assert False

    # notification: username does not exist
    else:
        assert False
