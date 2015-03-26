#!/usr/bin/python

## @jsonschema_definition.py
#  This file contains various jsonschema definitions.

## jsonschema_number(): ensures integer validation.
def jsonschema_number():
    schema = {
        'type': 'object',
        'properties': {
            'value': {
                'type': 'number',
                'minLength': 1
            },
        },
    }
    return schema

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

## jsonschema_posint(): ensures nonempty positive integer validation.
#
#  @exclusiveMinimum, ensures that the minimum is included with the minimum range.
def jsonschema_posint():
    schema = {
        'type': 'object',
        'properties': {
            'value': {
                'type': 'integer',
                'minimum': 0,
                'exclusiveMinimum': True,
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
                'enum': ['data_new', 'data_append', 'model_generate', 'model_use']
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
                'enum': ['data_new', 'data_append', 'model_generate', 'model_use']
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
        },
    }
    return schema

## jsonschema_model_use(): contains the jsonschema for the 'model_use' session.
#                          Therefore, this schema validates the properties
#                          describing the session, not the dataset itself.
#
#  Note: This validation schema is used in the corresponding validator_xxx.py.
def jsonschema_model_use():
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
            'svm_indep_variable': {
                'type': 'array',
                'items': { 'type': 'string' },
                'minItems': 1
            },
        },
    }
    return schema
