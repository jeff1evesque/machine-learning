#!/usr/bin/python

'''

This file contains various jsonschema dataset definitions.

'''


def schema_svm():
    '''

    This function validates svm dataset(s).

    '''

    schema = {
        'type': 'array',
        'minItems': 1,
        'additionalProperties': {
            'dependent-variable': {
                'type': 'string',
                'minLength': 1
            },
            'independent-variables': {
                'type': 'array',
                'minItems': 1,
                'additionalProperties': {
                    'type': 'string',
                    'minLength': 1
                }
            }
        }
    }
    return schema

def schema_svr():
    '''

    This function validates svr dataset(s).

    '''

    schema = {
        'type': 'array',
        'minItems': 1,
        'additionalProperties': {
            'dependent-variable': {
                'type': 'number'
            },
            'independent-variables': {
                'type': 'array',
                'minItems': 1,
                'additionalProperties': {
                    'type': 'number'
                }
            }
        }
    }
    return schema
