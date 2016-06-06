#!/usr/bin/python

'''@save_feature_count'''

from brain.validator.validate_file_extension import Validate_File_Extension


def reduce_dataset(dataset, session_type):
    '''@reduce_dataset

    This method validates the file extension for each uploaded dataset,
    and returns the unique (non-duplicate) dataset.

    '''

    # variables
    list_error = []

    # web-interface: validate, and restructure dataset
    if dataset['data']['dataset']['file_upload']:
        validator = Validate_File_Extension(
            dataset,
            session_type
        )
        adjusted_dataset = validator.validate()

        if adjusted_dataset['error']:
            list_error.append(
                adjusted_dataset['error']
            )

    # programmatic-interface: validate, do not restructure
    elif dataset['data']['dataset']['json_string']:
        adjusted_dataset = dataset['data']

        if dataset['error']:
            list_error.append(adjusted_dataset['error'])

    # return
    if list_error:
        return {'dataset': None, 'error': list_error}
    else:
        return {'dataset': adjusted_dataset, 'error': None}
