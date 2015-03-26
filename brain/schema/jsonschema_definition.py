#!/usr/bin/python

## @jsonschema_definition.py
#  This file contains various jsonschema definitions.

## jsonschema_int(): ensures integer validation.
def jsonschema_int():
    schema = {
        'type': 'object',
        'properties': {
            'value': 'integer',
            'minLength': 1
        },
    }
    return schema

## jsonschema_string(): ensures nonempty string validation.
def jsonschema_string():
    schema = {
        'type': 'object',
        'properties': {
            'value': 'string',
            'minLength': 1
        },
    }
    return schema

## jsonschema_dataset_id(): contains the jsonschema for the SVM dataset. Specifically,
#                           this schema complements the 'jsonschema_data_new()', and
#                           'jsonschema_data_append()' schemas, respectively.
#
#  Note: This validation schema is used in the corresponding validator_xxx.py.
#
#  @exclusiveMinimum, ensures that the minimum is included with the minimum range.
def jsonschema_dataset_id():
    schema = {
        'type': 'object',
        'properties': {
            'id_entity': {
                'type': 'integer',
                'minimum': 0,
                'exclusiveMinimum': true
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
