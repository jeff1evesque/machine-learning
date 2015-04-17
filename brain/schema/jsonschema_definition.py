#!/usr/bin/python

## @jsonschema_definition.py
#  This file contains various jsonschema definitions.

## jsonschema_string(): ensures nonempty string validation.
def jsonschema_string():
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

## jsonschema_data_new(): contains the jsonschema for the 'data_new' session.
#                         Therefore, this schema validates the properties
#                         describing the session, not the dataset itself.
#
#  Note: This validation schema is used in corresponding validator_xxx.py.
def jsonschema_data_new():
    schema = {
        'type': 'object',
        'properties': {
                'svm_title': {
                'type': 'string',
                'minLength': 1
            },
            'svm_session_id' : {
                'type': 'string',
                'minLength': 1
            },
            'svm_dataset_type': {
                'type': 'string',
                'enum': ['file_upload', 'dataset_url']
            },
            'svm_session': {
                'type': 'string',
                'enum': ['data_new', 'data_append', 'model_generate', 'model_predict']
            },
        },
    }
    return schema

## jsonschema_data_append(): contains the jsonschema for the 'data_new' session.
#                            Therefore, this schema validates the properties
#                            describing the session, not the dataset itself.
#
#  Note: This validation schema is used in corresponding validator_xxx.py.
def jsonschema_data_append():
    schema = {
        'type': 'object',
        'properties': {
            'svm_session_id': {
                'type': 'string',
                'minLength': 1
            },
            'svm_dataset_type': {
                'type': 'string',
                'enum': ['file_upload', 'dataset_url']
            },
            'svm_session': {
                'type': 'string',
                'enum': ['data_new', 'data_append', 'model_generate', 'model_predict']
            },
        },
    }
    return schema

## jsonschema_model_generate(): contains the jsonschema for the 'model_generate'
#                               session. Therefore, this schema validates the
#                               properties describing the session, not the dataset
#                               itself.
#
#  Note: This validation schema is used in the corresponding validator_xxx.py.
def jsonschema_model_generate():
    schema = {
        'type': 'object',
        'properties': {
            'svm_session_id': {
                'type': 'string',
                'minLength': 1
            },
            'svm_model_type': {
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

## jsonschema_model_predict(): contains the jsonschema for the 'model_predict'
#                              session. Therefore, this schema validates the
#                              properties describing the session, not the dataset
#                              itself.
#
#  Note: This validation schema is used in the corresponding validator_xxx.py.
def jsonschema_model_predict():
    schema = {
        'type': 'object',
        'properties': {
            'svm_title': {'type': 'string'},
            'svm_model_type': {
                'type': 'string',
                'enum': ['classification', 'regression']
            },
            'svm_session': {
                'type': 'string',
                'enum': ['training', 'analysis']
            },
        },
    }
    return schema
