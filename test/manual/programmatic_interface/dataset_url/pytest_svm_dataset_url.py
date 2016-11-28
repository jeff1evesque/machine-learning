'''@pytest_svm_dataset_url

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

    root = '/vagrant'
    json_dataset = None

    with open(
        root + '/' +
        os.path.join(
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


def test_data_new():
    '''@test_data_new

    This method tests the 'data_new' session.

    '''

    assert requests.post(
        endpoint_url,
        headers=headers,
        data=get_sample_json('svm-data-new.json', 'svm')
    )


def test_data_append():
    '''@test_data_append

    This method tests the 'data_append' session.

    '''

    assert requests.post(
        endpoint_url,
        headers=headers,
        data=get_sample_json('svm-data-append.json', 'svm')
    )


def test_model_generate():
    '''@test_model_generate

    This method tests the 'model_generate' session.

    '''

    assert requests.post(
        endpoint_url,
        headers=headers,
        data=get_sample_json('svm-model-generate.json', 'svm')
    )


def test_model_predict():
    '''@test_model_predict

    This method tests the 'model_predict' session.

    '''

    assert requests.post(
        endpoint_url,
        headers=headers,
        data=get_sample_json('svm-model-predict.json', 'svm')
    )
