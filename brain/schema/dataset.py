#!/usr/bin/python

'''

This file validates the supplied dataset.

'''

from voluptuous import Schema, Required, Optional, All, Any, Length


def validate_svm(data):
    '''

    This function validates svm dataset(s).

    '''

    schema = Schema([
        {
            Required('dependent-variable'): All(unicode, Length(min=1)),
            Required('independent-variables'): [{
                Required(All(unicode, Length(min=1))): Any(int, float),
            }],
        },
    ])

    schema(data)

def validate_svr(data):
    '''

    This function validates svr dataset(s).

    '''

    schema = Schema([
        {
            Required('dependent-variable'): Any(int, float),
            Required('independent-variables'): [{
                Required(All(unicode, Length(min=1))): Any(int, float),
            }],
        },
    ])

    schema(data)
