#!/usr/bin/python

'''

This file contains various jsonschema definitions.

'''

from voluptuous import Schema, Required, Optional, All, Length


def schema_data_new():
    '''

    This method validates the 'data_new' session, by validating the session
    properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    return Schema({
        Required('session_name'): All(str, Length(min=1)),
        Required('collection'): All(str, Length(min=1)),
        Required('dataset_type'): ['file_upload', 'dataset_url', 'json_string'],
        Required('session_type'): ['data_new'],
        Required('model_type'): ['svm', 'svr'],
        Optional('stream'): ['true', 'false'],
    })


def schema_data_append():
    '''

    This method validates the 'data_append' session, by validating the session
    properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    return Schema({
        Required('collection'): All(str, Length(min=1)),
        Required('dataset_type'): ['file_upload', 'dataset_url', 'json_string'],
        Required('session_type'): ['data_append'],
        Required('model_type'): ['svm', 'svr'],
        Optional('stream'): ['true', 'false'],
    })


def schema_model_generate():
    '''

    This method validates the 'model_generate' session, by validating the
    session properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    return Schema({
        Required('properties'): {
            Required('session_id'): All(str, Length(min=1)),
            Required('sv_model_type'): ['svm', 'svr'],
            Required('session_type'): ['model_generate'],
        }
    })


def schema_model_predict():
    '''

    This method validates the 'model_predict' session, by validating the
    session properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    return Schema({
        Required('properties'): {
            Required('session_type'): ['model_generate'],
            Required('collection'): All(str, Length(min=1)),
        }
    })
