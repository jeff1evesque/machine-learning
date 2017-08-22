'''

This file will test specific database limitations. More generally, it will test
conditions when a user chooses to store a new collection of documents, or when
users elect to append additional documents, into a preexisting collection. The
following svm cases for both anonymous and, authenticated users will be tested:

  - users have exceeded maximum collections
    - anon: oldest collection will be removed, from corresponding database(s),
            prior to saving the new proposed collection
    - auth: new collection will not save, unless the user chooses to manually
            delete a previous collection of their choice

  - users have exceeded maximum documents in a collections
    - anon: new documents will not save, in the proposed collection
    - auth: new documents will not save, unless the user chooses to manually
            delete a previous document, in the proposed collection

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

import json
import os.path
from flask import current_app, url_for
from brain.database.entity import Entity
from brain.database.dataset import import Collection


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
            'dataset_url',
            jsonfile
        ),
        'r'
    ) as json_file:
        json_dataset = json.load(json_file)

    return json.dumps(json_dataset)


def test_max_collections_anon(client, live_server):
    '''

    This method will test when an anonymous user, has exceeded the maximum
    allowed collection. In such a case, the oldest collection will be removed,
    to allow the proposed collection to be stored in the corresponding
    database(s).

    '''

    @live_server.app.route('/load-data')
    def get_endpoint():
        return url_for('name.load_data', _external=True)

    live_server.start()

    # local variables
    entity = Entity()
    collection = Collection()
    max_collection = current_app.config.get('MAXCOL_ANON')

    # save max collection
    for i in range(max_collection):
        dataset = get_sample_json('svm-data-new.json', 'svm')
        dataset['properties']['collection'] = 'collection--pytest-svm--' + str(i)

        res = client.post(
            get_endpoint(),
            headers={'Content-Type': 'application/json'},
            data=dataset
        )

        # assertion checks
        assert res.status_code == 200
        assert res.json['status'] == 0

    # save max collection + 1
    dataset = get_sample_json('svm-data-new.json', 'svm')
    dataset['properties']['collection'] = 'collection--pytest-svm--' + str(i + 1)

    res = client.post(
        get_endpoint(),
        headers={'Content-Type': 'application/json'},
        data=dataset
    )

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0
    assert entity.get_collection_count(0) == max_collection
    assert collection.query('collection--pytest-svm--' + str(i + 1), 'find_one')

    # drop all collections
    for i in range(max_collection):
        assert entity.remove_entity(0, 'collection--pytest-svm--' + str(i + 1))
        assert collection.query(
            'collection--pytest-svm--' + str(i + 1),
            'drop_collection'
        )


def test_max_collections_auth(client, live_server):
    '''

    This method will test when an authenticated user, has exceeded the maximum
    allowed collection. In such a case, the proposed collection will not to be
    stored in the corresponding database(s). Instead, the authenticated user,
    will need to manually delete a chosen collection, using constructs of the
    corresponding web-interface, or exposed programmatic-api, to allow the
    proposed collection to be stored in the corresponding database(s).

    '''

    @live_server.app.route('/load-data')
    def get_endpoint():
        return url_for('name.load_data', _external=True)

    live_server.start()

    # local variables
    entity = Entity()
    collection = Collection()
    max_collection = current_app.config.get('MAXCOL_AUTH')

    # save max collection
    for i in range(max_collection):
        dataset = get_sample_json('svm-data-new.json', 'svm')
        dataset['properties']['collection'] = 'collection--pytest-svm--' + str(i)

        res = client.post(
            get_endpoint(),
            headers={'Content-Type': 'application/json'},
            data=dataset
        )

        # assertion checks
        assert res.status_code == 200
        assert res.json['status'] == 0

    # save max collection + 1
    dataset = get_sample_json('svm-data-new.json', 'svm')
    dataset['properties']['collection'] = 'collection--pytest-svm--' + str(i + 1)

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0
    assert entity.get_collection_count(1) == max_collection
    assert collection.query('collection--pytest-svm--' + str(i), 'find_one')
    assert not collection.query('collection--pytest-svm--' + str(i + 1), 'find_one')

    # drop all collections
    for i in range(max_collection):
        assert entity.remove_entity(1, 'collection--pytest-svm--' + str(i + 1))
        assert collection.query(
            'collection--pytest-svm--' + str(i + 1),
            'drop_collection'
        )
