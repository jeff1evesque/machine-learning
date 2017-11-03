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
a valid token value, to the ``/load-data`` endpoint, should correspond to
executing the following session, as an authenticated user:

- ``data-new``
- ``data-append``

The following unit tests, provides examples of the `flask-jwt <http://flask-jwt-extended.readthedocs.io/en/latest/>`_
implementation:

  - |login|_

.. |login| replace:: ``login``
.. _login: https://github.com/jeff1evesque/machine-learning/tree/master/test/live_server/1_authentication/pytest_4_user_login
  