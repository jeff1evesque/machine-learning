'''

This file will test specific database limitations. More generally, it will test
conditions when a user chooses to store a new collection of documents, or when
users elect to append additional documents, into a preexisting collection. The
following svm cases for anonymous users, will be tested:

  - users have exceeded maximum collections
    - anon: oldest collection will be removed, from corresponding database(s),
            prior to saving the new proposed collection

  - users have exceeded maximum documents in a collections
    - anon: new documents will not save, in the proposed collection

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

import json
import os.path
from flask import current_app, url_for


def get_sample_json(jsonfile, model_type):
    '''

    Get a sample json dataset.

    '''

    # local variables
    root = current_app.config.get('ROOT')

    # open file
    json_dataset = None

    with open(
        os.path.join(
            root,
            'interface',
            'static',
            'data',
            'json',
            'programmatic_interface',
            model_type,
            'file_upload',
            jsonfile
        ),
        'r'
    ) as json_file:
        json_dataset = json.load(json_file)

    return json_dataset


def login(client):
    '''

    This method twill login, and return the corresponding token.

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

def send_post(client, endpoint, dataset):
    '''

    This method will login, and return the corresponding token.

    '''

    token = login(client)
    return client.post(
        endpoint,
        headers={
            'Authorization': 'Bearer {0}'.format(token),
            'Content-Type': 'application/json'
        },
        data=json.dumps(dataset)
    )


def test_save(client, live_server):
    '''

    This method will test storing the 'max_collection' number of collections.

    '''

    @live_server.app.route('/load-data')
    def load_data():
        return url_for('api.load_data', _external=True)

    live_server.start()

    # local variables
    endpoint = load_data()
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # save max collection
    for i in range(max_collection):
        dataset = get_sample_json('svm-data-new.json', 'svm')
        dataset['properties']['collection'] = 'collection--pytest-svm--' + str(i)
        res = send_post(client, endpoint, json.dumps(dataset))

        # assertion checks
        assert res.status_code == 200
        assert res.json['status'] == 0


def test_document_count(client, live_server):
    '''

    This method will test whether the document count for each collection, does
    not exceed the 'max_collection' limit, after 'max_collection' number of
    collections have been saved.

    '''

    @live_server.app.route('/document-count')
    def document_count():
        return url_for('api.document_count', _external=True)

    live_server.start()

    # local variables
    endpoint = document_count()
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # save max collection
    for i in range(max_collection):
        data = json.dumps({'collection': 'collection--pytest-svm--' + str(i)})
        res = send_post(client, endpoint, data)

        assert res.status_code == 200
        assert res.json['count'] == 1


def test_collection_count(client, live_server):
    '''

    This method will test whether the specified user has not exceeded the
    'max_collection' limit, after 'max_collection' number of collections have
    been saved.

    '''

    @live_server.app.route('/collection-count')
    def collection_count():
        return url_for('api.collection_count', _external=True)

    live_server.start()

    # local variables
    endpoint = collection_count()
    max_collection = current_app.config.get('MAXCOL_AUTH')
    res = send_post(client, endpoint, json.dumps({'uid': 1}))

    assert res.status_code == 200
    assert res.json['count'] == max_collection


def test_save_plus(client, live_server):
    '''

    This method will test saving an additional collection, in addition to
    the previous 'max_collection' collections already saved. For anonymous
    users, the oldest (i.e. first) database collection related objects, will be
    removed, to satisfy the maximum number of collections allowed to be saved.

    '''

    @live_server.app.route('/load-data')
    def load_data():
        return url_for('api.load_data', _external=True)

    live_server.start()

    # local variables
    endpoint = load_data()
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # save max collection + 1
    dataset = get_sample_json('svm-data-new.json', 'svm')
    dataset['properties']['collection'] = 'collection--pytest-svm--' + str(max_collection)

    res = send_post(client, endpoint, json.dumps(dataset))

    assert res.status_code == 200
    assert res.json['status'] == 0


def test_collection_count_plus(client, live_server):
    '''

    This method will test whether the specified user has not exceeded the
    'max_collection' limit. Specifically, if 'max_collection + 1' is saved,
    then the oldest collection will be removed.

    '''

    @live_server.app.route('/collection-count')
    def collection_count():
        return url_for('api.collection_count', _external=True)

    live_server.start()

    # local variables
    endpoint = collection_count()
    max_collection = current_app.config.get('MAXCOL_AUTH')

    res = send_post(client, endpoint, json.dumps({'uid': 1}))

    assert res.status_code == 200
    assert res.json['count'] == max_collection


def test_document_count_plus(client, live_server):
    '''

    This method will test whether each collection, owned by the specified user,
    does not exceed the 'max_document' limit, after 'max_collection + 1' number
    of collections have been saved.

    '''

    @live_server.app.route('/document-count')
    def document_count():
        return url_for('api.document_count', _external=True)

    live_server.start()

    # local variables
    endpoint = document_count()
    max_collection = current_app.config.get('MAXCOL_AUTH')

    for i in range(max_collection + 1):
        res = send_post(
            client,
            endpoint,
            json.dumps({
                'collection': 'collection--pytest-svm--' + str(i)
            })
        )

        if i == 0:
            assert res.json['count'] == -1
        else:
            assert res.json['count'] == 1


def test_entity_drop(client, live_server):
    '''

    This method will test the response code, after removing all entities,
    associated with collections, within the 'max_collection' limit.

    '''

    @live_server.app.route('/remove-collection')
    def remove_collection():
        return url_for('api.remove_collection', _external=True)

    live_server.start()

    # local variables
    endpoint = remove_collection()
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # drop all entity related collections
    for i in range(max_collection - 1):
        res = send_post(
            client,
            endpoint,
            json.dumps({
                'uid': 1,
                'collection': 'collection--pytest-svm--' + str(i),
                'type': 'collection',
            })
        )

        assert res.status_code == 200


def test_collection_drop(client, live_server):
    '''

    This method will test the respone code, after removing all collections,
    within the 'max_collection' limit.

    '''

    @live_server.app.route('/remove-collection')
    def remove_collection():
        return url_for('api.remove_collection', _external=True)

    live_server.start()

    # local variables
    endpoint = remove_collection()
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # drop all collections
    for i in range(max_collection):
        res = send_post(
            client,
            endpoint,
            json.dumps({
                'uid': 1,
                'collection': 'collection--pytest-svm--' + str(i),
                'type': 'entity',
            })
        )

        assert res.status_code == 200


def test_document_count_removed(client, live_server):
    '''

    This method will test whether each collection, owned by the specified user,
    does not exceed the 'max_document' limit, after all collections have been
    removed.

    '''

    @live_server.app.route('/document-count')
    def document_count():
        return url_for('api.document_count', _external=True)

    live_server.start()

    # local variables
    endpoint = document_count()
    max_collection = current_app.config.get('MAXCOL_AUTH')

    for i in range(max_collection):
        res = send_post(
            client,
            endpoint,
            json.dumps({
                'collection': 'collection--pytest-svm--' + str(i),
            })
        )

        assert res.status_code == 200
        assert res.json['count'] == -1


def test_collection_count_removed(client, live_server):
    '''

    This method will test whether the specified user has not exceeded the
    'max_collection' limit, after all collections have been removed.

    '''

    @live_server.app.route('/collection-count')
    def collection_count():
        return url_for('api.collection_count', _external=True)

    live_server.start()

    # local variables
    endpoint = collection_count()
    res = send_post(client, endpoint, json.dumps({'uid': 1}))

    assert res.status_code == 200
    assert res.json['count'] == 0