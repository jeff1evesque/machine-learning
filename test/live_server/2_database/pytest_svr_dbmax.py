'''

This file will test specific database limitations. More generally, it will test
conditions when a user chooses to store a new collection of documents, or when
users elect to append additional documents, into a preexisting collection. The
following svr cases for anonymous users, will be tested:

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


def send_post(client, endpoint, token, data):
    '''

    This method will login, and return the corresponding token.

    @token, is defined as a fixture, in our 'conftest.py', to help reduce
        runtime on our tests.

    '''

    return client.post(
        endpoint,
        headers={
            'Authorization': 'Bearer {0}'.format(token),
            'Content-Type': 'application/json'
        },
        data=data
    )


def test_save(client, live_server, token):
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
        dataset = get_sample_json('svr-data-new.json', 'svr')
        dataset['properties']['collection'] = 'collection--pytest-svr--' + str(i)
        res = send_post(client, endpoint, token, json.dumps(dataset))

        # assertion checks
        assert res.status_code == 200
        assert res.json['status'] == 0


def test_document_count(client, live_server, token):
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
        data = json.dumps({'collection': 'collection--pytest-svr--' + str(i)})
        res = send_post(client, endpoint, token, data)

        assert res.status_code == 200
        assert res.json['count'] == 1


def test_collection_count(client, live_server, token):
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
    res = send_post(client, endpoint, token, json.dumps({'uid': 1}))

    assert res.status_code == 200
    assert res.json['count'] == max_collection


def test_save_plus(client, live_server, token):
    '''

    This method will test whether any collections attempted to be saved, after
    the maximum allowed, will be ignored.

    Note: for anonymous users (pertains to web-interface), successive
          collections will be stored, causing the oldest collections to be
          iteratively removed.

    '''

    @live_server.app.route('/load-data')
    def load_data():
        return url_for('api.load_data', _external=True)

    live_server.start()

    # local variables
    endpoint = load_data()
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # save max collection + 1
    dataset = get_sample_json('svr-data-new.json', 'svr')
    dataset['properties']['collection'] = 'collection--pytest-svr--' + str(max_collection)

    res = send_post(client, endpoint, token, json.dumps(dataset))

    assert res.status_code == 200
    assert res.json['status'] == 0


def test_collection_count_plus(client, live_server, token):
    '''

    This method will test whether the specified user has not exceeded the
    'max_collection' limit. Specifically, if 'max_collection + 1' is saved,
    then successive collection will be ignored, and not saved.

    Note: for anonymous users (pertains to web-interface), successive
          collections will be stored, causing the oldest collections to be
          iteratively removed.

    '''

    @live_server.app.route('/collection-count')
    def collection_count():
        return url_for('api.collection_count', _external=True)

    live_server.start()

    # local variables
    endpoint = collection_count()
    max_collection = current_app.config.get('MAXCOL_AUTH')

    res = send_post(client, endpoint, token, json.dumps({'uid': 1}))

    assert res.status_code == 200
    assert res.json['count'] == max_collection


def test_document_count_plus(client, live_server, token):
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
            token,
            json.dumps({
                'collection': 'collection--pytest-svr--' + str(i)
            })
        )

        if i == max_collection:
            assert res.json['count'] == -1
        else:
            assert res.json['count'] == 1


def test_entity_drop(client, live_server, token):
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
    for i in range(max_collection):
        res = send_post(
            client,
            endpoint,
            token,
            json.dumps({
                'uid': 1,
                'collection': 'collection--pytest-svr--' + str(i),
                'type': 'collection',
            })
        )

        assert res.status_code == 200


def test_collection_drop(client, live_server, token):
    '''

    This method will test the response code, after removing all collections,
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
            token,
            json.dumps({
                'uid': 1,
                'collection': 'collection--pytest-svr--' + str(i),
                'type': 'entity',
            })
        )

        assert res.status_code == 200


def test_document_count_removed(client, live_server, token):
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
            token,
            json.dumps({
                'collection': 'collection--pytest-svr--' + str(i),
            })
        )

        assert res.status_code == 200
        assert res.json['count'] == -1


def test_collection_count_removed(client, live_server, token):
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
    res = send_post(client, endpoint, token, json.dumps({'uid': 1}))

    assert res.status_code == 200
    assert res.json['count'] == 0
