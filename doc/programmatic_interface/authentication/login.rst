=====
Login
=====

Users can submit a ``/login`` request, for the programmatic-api:

.. code:: python

    # request attributes
    username = 'jeff1evesque'
    password = 'password123'
    payload = {'user[login]': username, 'user[password]': password}

    # login and get flask-jwt token
    login = client.post(
        '/login',
        headers={'Content-Type': 'application/json'},
        data=payload
    )
    token = login.json['access_token']

The returned ``token`` value, can be supplied on successive requests, to a rest
endpoint, expecting the corresponding ``token`` value. For example, supplying
a valid token, to the ``/load-data`` endpoint:

.. code:: python

    # request attributes
    username = 'jeff1evesque'
    password = 'password123'
    payload = {'user[login]': username, 'user[password]': password}

    # login and get flask-jwt token
    login = client.post(
        'https://localhost:9090/login',
        headers={'Content-Type': 'application/json'},
        data=payload
    )
    token = login.json['access_token']

    # provide flask-jwt token
    res = client.post(
        'https://localhost:9090/load-data',
        headers={
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        },
        data=payload
    )

The following sessions, can be implemented with the above token, or omitted as
an anonymous user:

- `data-new <https://github.com/jeff1evesque/machine-learning/blob/master/doc/programmatic_interface/data/data_new.rst>`_
- `data-append <https://github.com/jeff1evesque/machine-learning/blob/master/doc/programmatic_interface/data/data_new.rst>`_

The following unit tests, provides examples of the `flask-jwt <http://flask-jwt-extended.readthedocs.io/en/latest/>`_
implementation:

- |pytest_6_user_session.py|_

.. |pytest_6_user_session.py| replace:: ``pytest_6_user_session.py``
.. _pytest_6_user_session.py: https://github.com/jeff1evesque/machine-learning/tree/master/test/live_server/1_authentication/pytest_6_user_login.py
  