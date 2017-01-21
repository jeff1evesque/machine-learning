'''

This file will test the necessary interfaces required to create a user account.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

from brain.validator.validate_password import validate_password
from brain.database.retrieve_account import Retrieve_Account
from brain.database.save_account import Save_Account
from brain.converter.crypto import hashpass


def test_registration(client, live_server):
    '''

    This method tests the user registration process.

    '''

    live_server.start()

    # local variables
    username = 'jeff1evesque'
    email = 'jeff1evesque@yahoo.com'
    password = 'password123'
    authenticate = Retrieve_Account()

    # verify requirements: one letter, one number, and ten characters.
    if (validate_password(password)):

        # validate: unique username
        if not authenticate.check_username(username)['result']:

            # validate: unique email
            if not authenticate.check_email(email)['result']:

                # database query: save username, and password
                hashed = hashpass(str(password))
                result = Save_Account().save_account(username, email, hashed)

                # notification: attempt to store account
                assert result['status']
                assert result['id']
                assert not result['error']

            # notification: email already exists
            else:
                assert False

        # notification: account already exists
        else:
            assert False

    # notification: password doesn't meet criteria
    else:
        assert False
