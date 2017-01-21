#!/usr/bin/python

'''

This file validates file extensions, as well as reducing supplied dataset(s).

'''

from brain.validator.validate_file_extension import Validate_File_Extension


def reduce_dataset(dataset, session_type):
    '''

    This method validates the file extension for each uploaded dataset,
    and returns the unique (non-duplicate) dataset.

    '''

    # variables
    list_error = []

    # web-interface: validate, and restructure 'file-upload' dataset
    if (
            dataset['data'].get('dataset', None) and
            dataset['data']['dataset'].get('file_upload', None) and
            dataset['data']['settings'].get(
                'dataset_type', None) == 'file_upload'
    ):

        # validate and restructure
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
    elif (
            dataset['data']['settings'].get('dataset[]', None) and
            dataset['data']['settings'].get(
                'dataset_type', None) == 'dataset_url'
    ):

        # define 'file_upload' since doesn't exist
        data = dataset['data']
        data['dataset'] = {}
        if type(data['settings']['dataset[]']) is list:
            data['dataset']['file_upload'] = data['settings']['dataset[]']
        else:
            data['dataset']['file_upload'] = []
            data['dataset']['file_upload'].append(
                data['settings']['dataset[]']
            )

        # validate and restructure
        validator = Validate_File_Extension(
            {
                'data': {
                    'dataset': {
                        'file_upload': data['dataset']['file_upload'],
                        'type': data['settings']['dataset_type'],
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
    elif (
            dataset['data']['dataset'].get('json_string', None) and
            dataset['data']['settings'].get(
                'dataset_type', None) == 'file_upload'
    ):

        adjusted_dataset = dataset['data']

        if dataset['error']:
            list_error.append(adjusted_dataset['error'])

    # programmatic-interface: validate, and restructure url dataset
    elif (
            dataset['data']['dataset'].get('json_string', None) and
            dataset['data']['settings'].get(
                'dataset_type', None) == 'dataset_url'
    ):

        # define 'file_upload' since doesn't exist
        data = dataset['data']
        if type(data['dataset']['json_string']) is list:
            data['dataset']['file_upload'] = data['dataset']['json_string']
        else:
            data['dataset']['file_upload'] = []
            data['dataset']['file_upload'].append(
                data['dataset']['json_string']
            )

        # validate and restructure
        validator = Validate_File_Extension(
            {
                'data': {
                    'dataset': {
                        'file_upload': data['dataset']['file_upload'],
                        'type': data['settings']['dataset_type'],
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

    # return
    if list_error:
        return {'dataset': None, 'error': list_error}
    else:
        return {'dataset': adjusted_dataset, 'error': None}
