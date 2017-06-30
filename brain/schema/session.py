#!/usr/bin/python

'''

This file contains various jsonschema definitions.

'''


def schema_data_new():
    '''

    This method validates the 'data_new' session, by validating the session
    properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    schema = {
        'type': 'object',
        'properties': {
            'session_name': {
                'type': 'string',
                'minLength': 1
            },
        },
        'session_id': {
            'type': 'string',
            'minLength': 1
        },
        'dataset_type': {
            'type': 'string',
            'enum': ['file_upload', 'dataset_url', 'json_string']
        },
        'session_type': {
            'type': 'string',
            'enum': ['data_new']
        },
    }
    return schema


def schema_data_append():
    '''

    This method validates the 'data_append' session, by validating the session
    properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    schema = {
        'type': 'object',
        'properties': {
            'session_id': {
                'type': 'string',
                'minLength': 1
            },
            'dataset_type': {
                'type': 'string',
                'enum': ['file_upload', 'dataset_url', 'json_string']
            },
            'session_type': {
                'type': 'string',
                'enum': ['data_append']
            },
        },
    }
    return schema


def schema_model_generate():
    '''

    This method validates the 'model_generate' session, by validating the
    session properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    schema = {
        'type': 'object',
        'properties': {
            'session_id': {
                'type': 'string',
                'minLength': 1
            },
            'sv_model_type': {
                'type': 'string',
                'enum': ['svm', 'svr']
            },
            'session_type': {
                'type': 'string',
                'enum': ['model_generate']
            },
        },
    }
    return schema


def schema_model_predict():
    '''

    This method validates the 'model_predict' session, by validating the
    session properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    schema = {
        'type': 'object',
        'properties': {
            'session_type': {
                'type': 'string',
                'enum': ['model_predict']
            },
        },
    }
    return schema
