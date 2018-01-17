#!/usr/bin/python

'''

This file validates each session properties.

'''

from voluptuous import Schema, Required, Optional, All, Any, Length


def validate_data_new(data):
    '''

    This method validates the 'data_new' session, by validating the session
    properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    schema = Schema({
        Required('collection'): All(unicode, Length(min=1)),
        Required('dataset_type'): Any('file_upload', 'dataset_url', 'json_string'),
        Required('model_type'): Any('svm', 'svr'),
        Required('session_type'): 'data_new',
        Required('session_name'): All(unicode, Length(min=1)),
        Optional('stream'): Any(True, False),
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
        Required('collection'): All(unicode, Length(min=1)),
        Required('dataset_type'): Any('file_upload', 'dataset_url', 'json_string'),
        Required('model_type'): Any('svm', 'svr'),
        Required('session_type'): 'data_append',
        Optional('stream'): Any(True, False),
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
        Required('collection'): All(unicode, Length(min=1)),
        Required('model_type'): Any('svm', 'svr'),
        Required('session_type'): 'model_generate',
        Optional('stream'): Any(True, False),
        Required('sv_kernel_type'): Any('linear', 'poly', 'rfb', 'sigmoid'),
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
        Required('collection'): All(unicode, Length(min=1)),
        Optional('stream'): Any(True, False),
        Required('prediction_input[]'): [
            All(unicode, Length(min=1)),
        ],
        Required('session_type'): 'model_predict',
    })
    schema(data)
