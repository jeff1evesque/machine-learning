'''@pytest_svm_dataset_url

This file will test the following svm sessions:
  - data_new: stores supplied dataset into a SQL database.
  - data_append: appends supplied dataset to an already stored dataset in an
                 SQL database.
  - model_generate: generate an model by selecting a particular range of
                    dataset (session), and store it into a NoSQL cache.
  - model_predict: generate a prediction by selecting a particular cached
                   model from the NoSQL cache.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

import json
import pytest
import os.path
from flask import url_for
from flask import current_app


def get_sample_json(jsonfile, model_type):
    '''@get_sample_json

    Get a sample json dataset.

    '''

    # local variables
    root = current_app.config.get('ROOT')

    # open file
    json_dataset = None

    try:
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

    except Exception as error:
        pytest.fail(error)

    return json.dumps(json_dataset)


def test_data_new(client, live_server):
    '''@test_data_new

    This method tests the 'data_new' session.

    '''

    @live_server.app.route('/load-data')
    def get_endpoint():
        return url_for('name.load_data', _external=True)

    live_server.start()

    res = client.post(
        get_endpoint(),
        headers={'Content-Type': 'application/json'},
        data=get_sample_json('svm-data-new.json', 'svm')
    )

    assert res.status_code == 200 and res.json['status'] == 0


def test_data_append(client, live_server):
    '''@test_data_append

    This method tests the 'data_new' session.

    '''

    @live_server.app.route('/load-data')
    def get_endpoint():
        return url_for('name.load_data', _external=True)

    live_server.start()

    res = client.post(
        get_endpoint(),
        headers={'Content-Type': 'application/json'},
        data=get_sample_json('svm-data-append.json', 'svm')
    )

    assert res.status_code == 200 and res.json['status'] == 0


def test_model_generate(client, live_server):
    '''@test_model_generate

    This method tests the 'model_generate' session.

    '''

    @live_server.app.route('/load-data')
    def get_endpoint():
        return url_for('name.load_data', _external=True)

    live_server.start()

    res = client.post(
        get_endpoint(),
        headers={'Content-Type': 'application/json'},
        data=get_sample_json('svm-model-generate.json', 'svm')
    )

    assert res.status_code == 200 and res.json['status'] == 0


def test_model_predict(client, live_server):
    '''@test_model_predict

    This method tests the 'model_predict' session.

    '''

    @live_server.app.route('/load-data')
    def get_endpoint():
        return url_for('name.load_data', _external=True)

    live_server.start()

    res = client.post(
        get_endpoint(),
        headers={'Content-Type': 'application/json'},
        data=get_sample_json('svm-model-predict.json', 'svm')
    )

    print json.loads(res.json['result']['confidence'])
    assert (
        res.status_code == 200 and
        res.json['status'] == 0 and
        res.json['result'] and
        res.json['result']['confidence'] and
        res.json['result']['confidence']['classes'] == [
            'dep-variable-1',
            'dep-variable-2',
            'dep-variable-3',
            'dep-variable-4',
            'dep-variable-5'
        ] and
        res.json['result']['confidence']['model'] == 'svm' and
        res.json['result']['confidence']['result'] == 'dep-variable-4'
    )
