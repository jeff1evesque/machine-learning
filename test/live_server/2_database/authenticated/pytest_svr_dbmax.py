'''

This file will test specific database limitations. More generally, it will test
conditions when a user chooses to store a new collection of documents, or when
users elect to append additional documents, into a preexisting collection. The
following svr cases for authenticated users, will be tested:

  - users have exceeded maximum collections
    - auth: new collection will not save, unless the user chooses to manually
            delete a previous collection of their choice

  - users have exceeded maximum documents in a collections
    - auth: new documents will not save, unless the user chooses to manually
            delete a previous document, in the proposed collection

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


def test_save(client, live_server):
    '''

    This method will test storing the 'max_collection' number of collections.

    '''

    @live_server.app.route('/load-data')
    def load_data():
        return url_for('name.load_data', _external=True)

    live_server.start()

    # local variables
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # save max collection
    for i in range(max_collection):
        dataset = get_sample_json('svr-data-new.json', 'svr')
        dataset['properties']['collection'] = 'collection--pytest-svr--' + str(i)

        res = client.post(
            load_data(),
            headers={'Content-Type': 'application/json'},
            data=json.dumps(dataset)
        )

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
        return url_for('name.document_count', _external=True)

    live_server.start()

    # local variables
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # save max collection
    for i in range(max_collection):
        res = client.post(
            document_count(),
            headers={'Content-Type': 'application/json'},
            data=json.dumps({
                'collection': 'collection--pytest-svr--' + str(i),
            })
        )

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
        return url_for('name.collection_count', _external=True)

    live_server.start()

    # local variables
    uid = 1
    max_collection = current_app.config.get('MAXCOL_AUTH')

    res = client.post(
        collection_count(),
        headers={'Content-Type': 'application/json'},
        data=json.dumps({'uid': uid})
    )

    assert res.status_code == 200
    assert res.json['count'] == max_collection


def test_save_plus(client, live_server):
    '''

    This method will test whether saving an additional collection is ignored,
    when an authenticated user, attempts to save a collection, given that
    'max_collection' collections already been saved. Functionally, users will
    need to explicitly choose an exact collection to remove, if they have
    already reached the corresponding 'max_collection' limit.

    '''

    @live_server.app.route('/load-data')
    def load_data():
        return url_for('name.load_data', _external=True)

    live_server.start()

    # local variables
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # save max collection + 1
    dataset = get_sample_json('svr-data-new.json', 'svr')
    dataset['properties']['collection'] = 'collection--pytest-svr--' + str(max_collection)

    res = client.post(
        load_data(),
        headers={'Content-Type': 'application/json'},
        data=json.dumps(dataset)
    )

    assert res.status_code == 200
    assert res.json['status'] == 0


def test_collection_count_plus(client, live_server):
    '''

    This method will test whether the specified user has not exceeded the
    'max_collection' limit. Specifically, attempting to save any further
    instances, beyond the latter limit, will be ignored.

    '''

    @live_server.app.route('/collection-count')
    def collection_count():
        return url_for('name.collection_count', _external=True)

    live_server.start()

    # local variables
    uid = 1
    max_collection = current_app.config.get('MAXCOL_AUTH')

    res = client.post(
        collection_count(),
        headers={'Content-Type': 'application/json'},
        data=json.dumps({'uid': uid})
    )

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
        return url_for('name.document_count', _external=True)

    live_server.start()

    # local variables
    max_collection = current_app.config.get('MAXCOL_AUTH')

    res = client.post(
        document_count(),
        headers={'Content-Type': 'application/json'},
        data=json.dumps({
            'collection': 'collection--pytest-svr--' +  str(max_collection),
        })
    )

    assert res.status_code == 200
    assert res.json['count'] == -1


def test_entity_drop(client, live_server):
    '''

    This method will test the response code, after removing all entities,
    associated with collections, within the 'max_collection' limit.

    '''

    @live_server.app.route('/remove-collection')
    def remove_collection():
        return url_for('name.remove_collection', _external=True)

    live_server.start()

    # local variables
    uid = 1
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # drop all entity related collections
    for i in range(max_collection):
        res = client.post(
            remove_collection(),
            headers={'Content-Type': 'application/json'},
            data=json.dumps({
                'uid': uid,
                'collection': 'collection--pytest-svr--' + str(i),
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
        return url_for('name.remove_collection', _external=True)

    live_server.start()

    # local variables
    uid = 1
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # drop all collections
    for i in range(max_collection):
        res = client.post(
            remove_collection(),
            headers={'Content-Type': 'application/json'},
            data=json.dumps({
                'uid': uid,
                'type': 'entity',
                'collection': 'collection--pytest-svr--' + str(i),
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
        return url_for('name.document_count', _external=True)

    live_server.start()

    # local variables
    max_collection = current_app.config.get('MAXCOL_AUTH')

    for i in range(max_collection):
        res = client.post(
            document_count(),
            headers={'Content-Type': 'application/json'},
            data=json.dumps({
                'collection': 'collection--pytest-svr--' + str(i),
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
        return url_for('name.collection_count', _external=True)

    live_server.start()

    # local variables
    uid = 1

    res = client.post(
        collection_count(),
        headers={'Content-Type': 'application/json'},
        data=json.dumps({'uid': uid})
    )

    assert res.status_code == 200
    assert res.json['count'] == 0
