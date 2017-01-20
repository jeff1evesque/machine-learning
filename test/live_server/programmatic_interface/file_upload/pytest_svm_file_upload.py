'''@pytest_svm_session

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
                'file_upload',
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

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


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

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


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

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


def test_model_predict(client, live_server):
    '''@test_model_predict

    This method tests the 'model_predict' session.

    Note: for debugging, the following syntax will output the corresponding
          json values, nested within 'json.loads()', to the travis ci:

          raise ValueError(res.json['result']['key1'])

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

    # check each probability is within acceptable margin
    fixed_prob = [
        0.3090315561788815,
        0.05089304164409372,
        0.30885779009321146,
        0.042701621539446635,
        0.28851599054436644
    ]
    cp = res.json['result']['confidence']['probability']
    margin_prob = 0.00007
    check_prob = [
        i for i in fixed_prob if any(abs(i-j) > margin_prob for j in cp)
    ]

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0
    assert res.json['result']
    assert res.json['result']['confidence']
    assert res.json['result']['confidence']['classes'] == [
        'dep-variable-1',
        'dep-variable-2',
        'dep-variable-3',
        'dep-variable-4',
        'dep-variable-5'
    ]
    assert res.json['result']['confidence']['decision_function'] == [
        0.2176409363746643,
        0.0,
        -0.2201467913263242,
        -0.22014661657537662,
        -0.2176409363746643,
        -0.49999960156529255,
        -0.4999994180301428,
        -0.2201467913263242,
        -0.22014661657537662,
        1.8353514974478458e-07
    ]
    assert check_prob
    assert res.json['result']['confidence']['model'] == 'svm'
    assert res.json['result']['confidence']['result'] == 'dep-variable-4'
