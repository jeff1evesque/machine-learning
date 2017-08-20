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
