'''@pytest_svr_file_upload

This module will test the following sessions:

  - data_new: stores supplied dataset into a SQL database.
  - data_append: appends supplied dataset to an already stored dataset in an
                 SQL database.
  - model_generate: generate an model by selecting a particular range of
                    dataset (session), and store it into a NoSQL cache.
  - model_predict: generate a prediction by selecting a particular cached
                   model from the NoSQL cache.

  Note: this module requires the installation of 'pytest':
      - pip install pytest

  Then, this script can be run as follows:
      - py.test session.py
      - py.test /some_directory

  Note: pytest will recursively check subdirectories for python scripts, from
        the current working directory.

  Note: this module is recommended to be run from the directory containing the
        'pytest.ini', as the current working directory.

'''

import requests
import json
import os.path

endpoint_url = 'http://localhost:5000/load-data'
headers = {'Content-Type': 'application/json'}


def get_sample_json(jsonfile, model_type):
    '''@get_sample_json

    Get a sample json dataset.

    '''

    # local variables
    root = '/vagrant'
    json_dataset = None

    # open file
    with open(
        root + '/' +
        os.path.join(
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

    return json.dumps(json_dataset)


def test_data_new():
    '''@test_data_new

    This method tests the 'data_new' session.

    '''

    res = requests.post(
        endpoint_url,
        headers=headers,
        data=get_sample_json('svr-data-new.json', 'svr')
    )

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


def test_data_append():
    '''@test_data_append

    This method tests the 'data_append' session.

    '''

    res = requests.post(
        endpoint_url,
        headers=headers,
        data=get_sample_json('svr-data-append.json', 'svr')
    )

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


def test_model_generate():
    '''@test_model_generate

    This method tests the 'model_generate' session.

    '''

    res = requests.post(
        endpoint_url,
        headers=headers,
        data=get_sample_json('svr-model-generate.json', 'svr')
    )

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


def test_model_predict():
    '''@test_model_predict

    This method tests the 'model_predict' session.

    '''

    res = requests.post(
        endpoint_url,
        headers=headers,
        data=get_sample_json('svr-model-predict.json', 'svr')
    )

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0
    assert res.json['result']
    assert res.json['result']['confidence']
    assert res.json['result']['confidence']['score'] == '0.97326950222129949'
    assert res.json['result']['model'] == 'svr'
    assert res.json['result']['result'] == '294.71600377'

