'''

This file will test the necessary interfaces during a login session.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

from flask import session
from brain.cache.query import Query


def test_session(client, live_server):
    '''

    This method tests whether a redis entry is created, to represent a user
    session, for the duration of a user login.

    '''

    live_server.start()

    # local variables
    username = 'jeff1evesque'
    password = 'password123'
    payload = {'user[login]': username, 'user[password]': password}

    # check redis for session
    login = client.post('/login', data=payload)

    if session.get('uid'):
        rcon = Query(0, 'redis', 6379)
        rcon.start_redis()
        raise Exception('login: ' + repr(login))
    else:
        assert False

    # check logout succeeded
    assert login.status_code == 200
    assert logout.status_code == 200
    assert not session.get('uid')
