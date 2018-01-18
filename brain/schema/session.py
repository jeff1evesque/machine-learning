#!/usr/bin/python

'''

This file validates each session properties.

'''

from flask import current_app
from voluptuous import Schema, Required, Optional, All, Any, In, Length


def validate_data_new(data):
    '''

    This method validates the 'data_new' session, by validating the session
    properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    model_type = current_app.config.get('MODEL_TYPE')
    dataset_type = current_app.config.get('DATASET_TYPE')
    schema = Schema({
        Required('collection'): All(unicode, Length(min=1)),
        Required('dataset_type'): In(dataset_type),
        Required('model_type'): In(model_type),
        Required('session_type'): 'data_new',
        Required('session_name'): All(unicode, Length(min=1)),
        Optional('stream'): Any('True', 'False'),
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

    model_type = current_app.config.get('MODEL_TYPE')
    dataset_type = current_app.config.get('DATASET_TYPE')
    schema = Schema({
        Required('collection'): All(unicode, Length(min=1)),
        Required('dataset_type'): In(dataset_type),
        Required('model_type'): In(model_type),
        Required('session_type'): 'data_append',
        Optional('stream'): Any('True', 'False'),
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

    model_type = current_app.config.get('MODEL_TYPE')
    sv_kernel_type = current_app.config.get('SV_KERNEL_TYPE')
    schema = Schema({
        Required('collection'): All(unicode, Length(min=1)),
        Required('model_type'): In(model_type),
        Required('session_type'): 'model_generate',
        Optional('stream'): Any('True', 'False'),
        Required('sv_kernel_type'): In(sv_kernel_type),
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
        Optional('stream'): Any('True', 'False'),
        Required('prediction_input[]'): [
            All(unicode, Length(min=1)),
        ],
        Required('session_type'): 'model_predict',
    })
    schema(data)
