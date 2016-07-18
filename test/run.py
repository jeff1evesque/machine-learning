'''@manager

This file implements the 'Manager' instance, which allows external scripts to
    be run within the corresponding flask script.  Specifically, 'pytest' is
    used to perform corresponding unit testing.

Note: the 'Manager', and 'pytest' instances can further be reviewed:

    - https://flask-script.readthedocs.io/en/latest/
    - http://docs.pytest.org/en/latest/usage.html

'''

import urllib2
from flask import Flask, url_for
import pytest
import json
import os.path

def test_add_endpoint_to_live_server(accept_json, client, live_server):
    @live_server.app.route('/load-data/')
    def get_endpoint():
        return url_for('name.load_data', _external=True)

    live_server.start()

    res = client.post(
        get_endpoint(),
        headers={'Content-Type': 'application/json'},
        data=get_sample_json('svm-data-new.json', 'svm')
    )
    print res.status_code
    assert res.status_code == 200

def get_sample_json(jsonfile, model_type):
    '''@get_sample_json

    Get a sample json dataset.

    '''

    json_dataset = None
    with open(
        '/vagrant/' + os.path.join(
            'interface',
            'static',
            'data',
            'json',
            'programmatic_interface',
            model_type,
            jsonfile
        ),
        'r'
    ) as json_file:
        json_dataset = json.load(json_file)
    return json.dumps(json_dataset)
