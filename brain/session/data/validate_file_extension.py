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

    # web-interface: validate, and restructure 'file-upload' dataset
    if (
            dataset['data'].get('dataset', None) and
            dataset['data']['dataset'].get('file_upload', None)
        ):
        validator = Validate_File_Extension(
            dataset,
            session_type
        )
        adjusted_dataset = validator.validate()

        if adjusted_dataset['error']:
            list_error.append(
                adjusted_dataset['error']
            )

    # web-interface: validate, and restructure url dataset
    elif dataset['data']['settings'].get('dataset[]', None):
        urls = dataset['data']['settings']['dataset[]']
        validator = Validate_File_Extension(
            {
                'data': {
                    'dataset': {
                        'urls': urls,
                    }
                },
            },
            session_type
        )
        adjusted_dataset = validator.validate()

        if adjusted_dataset['error']:
            list_error.append(
                adjusted_dataset['error']
            )

    # programmatic-interface: validate, do not restructure file upload
    elif dataset['data']['dataset']['json_string']:
        adjusted_dataset = dataset['data']

        if dataset['error']:
            list_error.append(adjusted_dataset['error'])

    # programmatic-interface: validate, and restructure url dataset

    # return
    if list_error:
        return {'dataset': None, 'error': list_error}
    else:
        return {'dataset': adjusted_dataset, 'error': None}
