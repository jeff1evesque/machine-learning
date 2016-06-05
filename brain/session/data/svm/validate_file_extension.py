#!/usr/bin/python

'''@save_feature_count'''

from brain.validator.validate_file_extension import Validate_File_Extension


def svm_file_extension(self, dataset, session_type):
    '''@svm_file_extension

    This method validates the file extension for each uploaded dataset,
    and returns the unique (non-duplicate) dataset.

    '''

    # variables
    flag_upload = False
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
            flag_upload = True

    # programmatic-interface: validate, do not restructure
    elif dataset['data']['dataset']['json_string']:
        adjusted_dataset = dataset['data']

        if dataset['error']:
            list_error.append(self.premodel_data['error'])
            flag_upload = True

    # return
    if list_error:
        return {'dataset': None, 'error': list_error}
    else:
        return {'dataset': adjusted_dataset, 'error': None}
