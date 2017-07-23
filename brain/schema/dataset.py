#!/usr/bin/python

'''

This file contains various jsonschema dataset definitions.

'''


def schema_svm():
    '''

    This method validates svm dataset(s).

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

    This method validates svf dataset(s).

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
