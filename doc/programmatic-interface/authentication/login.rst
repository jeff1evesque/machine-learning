=====
Login
=====

Users can submit a ``/login`` request, for the programmatic rest-api:

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

The returned ``token``, will be required to be supplied on successive requests.
For example, supplying a valid token, to the ``/load-data`` endpoint:

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

**Note:** all programmatic rest endpoints (except ``/login``), requires a valid
token to be supplied, in order to properly submit a corresponding request.

The following sessions, can be implemented with the above token:

- `data-new <https://github.com/jeff1evesque/machine-learning/blob/master/doc/programmatic_interface/data/data_new.rst>`_
- `data-append <https://github.com/jeff1evesque/machine-learning/blob/master/doc/programmatic_interface/data/data_new.rst>`_
