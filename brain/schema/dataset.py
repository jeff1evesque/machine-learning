#!/usr/bin/python

'''

This file contains various jsonschema dataset definitions.

'''

from voluptuous import Schema, Required, Optional, All, Length


def schema_svm(data):
    '''

    This function validates svm dataset(s).

    '''

    schema = Schema([
        {
            Required('dataset'): [{
                Required('dependent-variable'): All(str, Length(min=1)),
                Required('independent-variable'): [{
                    Required(All(str, Length(min=1))): All(float, Length(min=1)),
                }],
            }],
        },
    ])

    schema(data)

def schema_svr(data):
    '''

    This function validates svr dataset(s).

    '''

    schema = Schema([
        {
            Required('dataset'): [{
                Required('dependent-variable'): All(float, Length(min=1)),
                Required('independent-variable'): [{
                    Required(All(str, Length(min=1))): All(float, Length(min=1)),
                }],
            }],
        },
    ])

    schema(data)
