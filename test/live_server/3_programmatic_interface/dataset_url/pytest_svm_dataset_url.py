'''

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
            'dataset_url',
            jsonfile
        ),
        'r'
    ) as json_file:
        json_dataset = json.load(json_file)

    return json.dumps(json_dataset)


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


def test_data_new(client, live_server, token):
    '''

    This method tests the 'data_new' session.

    '''

    @live_server.app.route('/load-data')
    def load_data():
        return url_for('api.load_data', _external=True)

    live_server.start()

    # local variables
    endpoint = load_data()

    res = send_post(
        client,
        endpoint,
        token,
        get_sample_json('svm-data-new.json', 'svm')
    )

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


def test_data_append(client, live_server, token):
    '''

    This method tests the 'data_new' session.

    '''

    @live_server.app.route('/load-data')
    def load_data():
        return url_for('api.load_data', _external=True)

    live_server.start()

    # local variables
    endpoint = load_data()

    res = send_post(
        client,
        endpoint,
        token,
        get_sample_json('svm-data-append.json', 'svm')
    )

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


def test_model_generate(client, live_server, token):
    '''

    This method tests the 'model_generate' session.

    '''

    @live_server.app.route('/load-data')
    def load_data():
        return url_for('api.load_data', _external=True)

    live_server.start()

    # local variables
    endpoint = load_data()

    res = send_post(
        client,
        endpoint,
        token,
        get_sample_json('svm-model-generate.json', 'svm')
    )

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


def test_model_predict(client, live_server, token):
    '''

    This method tests the 'model_predict' session.

    Note: for debugging, the following syntax will output the corresponding
          json values, nested within 'json.loads()', to the travis ci:

          raise ValueError(res.json['result']['key1'])

    '''

    @live_server.app.route('/load-data')
    def load_data():
        return url_for('api.load_data', _external=True)

    live_server.start()

    # local variables
    endpoint = load_data()

    res = send_post(
        client,
        endpoint,
        token,
        get_sample_json('svm-model-predict.json', 'svm')
    )

    # check each probability is within acceptable margin
    fixed_prob = [
        0.14075033321086294,
        0.14500955005546354,
        0.14156072707544004,
        0.19249135186767916,
        0.38018803779055466
    ]
    cp = res.json['result']['confidence']['probability']
    margin_prob = 0.005
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
        0.1221379769127864,
        0.0,
        -0.2201467913263242,
        -0.22014661657537662,
        -0.12213797691278638,
        -0.33333297925570843,
        -0.33333281615328886,
        -0.2201467913263242,
        -0.22014661657537662,
        1.8353514974478458e-07
    ]
    assert check_prob
    assert res.json['result']['model'] == 'svm'
    assert res.json['result']['result'] == 'dep-variable-4'
