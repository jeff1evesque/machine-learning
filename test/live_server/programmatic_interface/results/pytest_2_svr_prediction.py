'''

This file will test the following cases:
  - saving a proposed svr prediction.
  - retrieving a supposed generated svr prediction.
  - retrieving all svr prediction titles, with respect to a supplied userid.

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
            'results',
            jsonfile
        ),
        'r'
    ) as json_file:
        json_dataset = json.load(json_file)

    return json.dumps(json_dataset)


def test_save_prediction(client, live_server):
    '''

    This method saves an svm prediction.

    '''

    @live_server.app.route('/save-prediction')
    def get_endpoint():
        return url_for('name.save_prediction', _external=True)

    live_server.start()

    res = client.post(
        get_endpoint(),
        headers={'Content-Type': 'application/json'},
        data=get_sample_json('save-prediction.json', 'svr')
    )

    # assertion checks
    assert res.status_code == 200

    if res.json['status'] == '1':
        print 'Unsuccessful storing the prediction result.'
        assert False
    elif res.json['status'] == '2':
        print 'Status was not valid.'
        assert False
    elif res.json['status'] == '3':
        print 'Improper request submitted.'
        assert False
    else:
        assert res.json['status']


def test_retrieve_prediction(client, live_server):
    '''

    This method retrieves a stored svm prediction.

    '''

    @live_server.app.route('/retrieve-prediction')
    def get_endpoint():
        return url_for('name.retrieve_prediction', _external=True)

    live_server.start()

    res = client.post(
        get_endpoint(),
        headers={'Content-Type': 'application/json'},
        data=get_sample_json('retrieve-prediction.json', 'svr')
    )

    # assertion checks
    assert res.status_code == 200

    if res.json['status'] == '1':
        print 'Unsuccessful retrieval of specified prediction parameter.'
        assert False
    elif res.json['status'] == '2':
        print 'Improper request submitted.'
        assert False
    else:
        assert res.json['status']

    assert res.json['result'] == '166.001388043'
    assert res.json['r2'] == '0.99114929281077535'


def test_retrieve_titles(client, live_server):
    '''

    This method retrieves all svm prediction titles, with respect to an
    identified userid (i.e. uid).

    '''

    @live_server.app.route('/retrieve-prediction-titles')
    def get_endpoint():
        return url_for('name.retrieve_prediction_titles', _external=True)

    live_server.start()

    res = client.post(
        get_endpoint(),
        headers={'Content-Type': 'application/json'},
        data=get_sample_json('retrieve-titles.json', 'svr')
    )

    # assertion checks
    assert res.status_code == 200

    if res.json['status'] == '1':
        print 'Unsuccessful retrieval of prediction titles'
        assert False
    elif res.json['status'] == '2':
        print 'Improper request submitted.'
        assert False
    else:
        assert res.json['status']

    assert res.json['title'] == ['svr-prediction-1']
