#!/usr/bin/python

'''@jsonschema_definition

This file contains various jsonschema definitions.

'''


def jsonschema_string():
    '''@jsonschema_string

    This method validates a non-empty string.

    '''

    schema = {
        'type': 'object',
        'properties': {
            'value': {
                'type': 'string',
                'minLength': 1
            },
        },
    }
    return schema


def jsonschema_data_new():
    '''@jsonschema_data_new

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
        'svm_dataset_type': {
            'type': 'string',
            'enum': ['file_upload', 'dataset_url', 'json_string']
        },
        'svm_session': {
            'type': 'string',
            'enum': ['data_new']
        },
    }
    return schema


def jsonschema_data_append():
    '''@jsonschema_data_new

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
            'svm_dataset_type': {
                'type': 'string',
                'enum': ['file_upload', 'dataset_url', 'json_string']
            },
            'svm_session': {
                'type': 'string',
                'enum': ['data_append']
            },
        },
    }
    return schema


def jsonschema_model_generate():
    '''@jsonschema_data_new

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
                'enum': ['classification', 'regression']
            },
            'svm_session': {
                'type': 'string',
                'enum': ['model_generate']
            },
        },
    }
    return schema


def jsonschema_model_predict():
    '''@jsonschema_data_new

    This method validates the 'model_predict' session, by validating the
    session properties, not the dataset itself.

    @file_upload, @dataset_url, are web-interface related values.

    @json_string, is a programmatic-interface related value.

    Note: This validation schema is used in corresponding validator_xxx.py.

    '''

    schema = {
        'type': 'object',
        'properties': {
            'svm_session': {
                'type': 'string',
                'enum': ['model_predict']
            },
        },
    }
    return schema
