'''@pytest_user_logout

This file will test the necessary interfaces required to logout.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

from flask import session


def test_logout(client, live_server):
    '''@test_logout

    This method tests the user logout process. It seems redundant, since it
    requires executing the login session. However, this login session is not
    identical to the login session test, which covers testing the username,
    and password requirements, along with the password hashing function. This
    test simply assumes the latter conditions have been met, and proceeds to
    testing if the logout would succeed, given the user can login.

    '''

    live_server.start()

    # local variables
    username = 'jeff1evesque'
    password = 'password123'
    payload = {'user[login]': username, 'user[password]': password}

    # post requests: login, and logout response
    login = client.post('/login', data=payload)
    if session.get('uid'):
        logout = client.post('/logout')
    else:
        assert False

    # check logout succeeded
    assert login.status_code == 200
    assert logout.status_code == 200
    assert not session.get('uid')
