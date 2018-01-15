#!/usr/bin/python

'''

This file validates each session properties.

'''

from voluptuous import Schema, Required, Optional, All, Length


def validate_data_new(data):
    '''

    This method validates the 'data_new' session, by validating the session
    properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    schema = Schema({
        Required('session_name'): All(str, Length(min=1)),
        Required('collection'): All(str, Length(min=1)),
        Required('dataset_type'): ['file_upload', 'dataset_url', 'json_string'],
        Required('session_type'): ['data_new'],
        Required('model_type'): ['svm', 'svr'],
        Optional('stream'): ['true', 'false'],
    })

    schema(data)


def validate_data_append(data):
    '''

    This method validates the 'data_append' session, by validating the session
    properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    schema = Schema({
        Required('collection'): All(str, Length(min=1)),
        Required('dataset_type'): ['file_upload', 'dataset_url', 'json_string'],
        Required('session_type'): ['data_append'],
        Required('model_type'): ['svm', 'svr'],
        Optional('stream'): ['true', 'false'],
    })

    schema(data)


def validate_model_generate(data):
    '''

    This method validates the 'model_generate' session, by validating the
    session properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    schema = Schema({
        Required('properties'): {
            Required('session_id'): All(str, Length(min=1)),
            Required('sv_model_type'): ['svm', 'svr'],
            Required('session_type'): ['model_generate'],
        }
    })

    schema(data)


def validate_model_predict(data):
    '''

    This method validates the 'model_predict' session, by validating the
    session properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    schema = Schema({
        Required('properties'): {
            Required('session_type'): ['model_generate'],
            Required('collection'): All(str, Length(min=1)),
        }
    })

    schema(data)
