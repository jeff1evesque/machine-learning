'''

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
    '''

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
    '''

    This method tests the 'data_new' session.

    '''

    res = requests.post(
        endpoint_url,
        headers=headers,
        data=get_sample_json('svm-data-new.json', 'svm')
    )

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


def test_data_append():
    '''

    This method tests the 'data_append' session.

    '''

    res = requests.post(
        endpoint_url,
        headers=headers,
        data=get_sample_json('svm-data-append.json', 'svm')
    )

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


def test_model_generate():
    '''

    This method tests the 'model_generate' session.

    '''

    res = requests.post(
        endpoint_url,
        headers=headers,
        data=get_sample_json('svm-model-generate.json', 'svm')
    )

    # assertion checks
    assert res.status_code == 200
    assert res.json['status'] == 0


def test_model_predict():
    '''

    This method tests the 'model_predict' session.

    '''

    res = requests.post(
        endpoint_url,
        headers=headers,
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
    assert res.json['result']['model'] == 'svm'
    assert res.json['result']['result'] == 'dep-variable-4'
