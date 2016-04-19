#!/usr/bin/python

'''@validate_file_extension

This script performs validation on the file extension for file upload(s), and
returns the validated temporary file references(s), along with the
corresponding file extension for each file upload(s).

'''

import os.path
from brain.converter.calculate_md5 import calculate_md5


class Validate_File_Extension(object):
    '''@Validate_File_Extension

    This class provides an interface to validate the file extension,
    associated with any file(s) representing the dataset.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, svm_data, svm_session=None):
        '''@__init__

        This constructor saves a subset of the passed-in form data.

        '''

        self.svm_data = svm_data
        self.svm_session = svm_session

    def validate(self):
        '''@validate

        This method validates the file extension, associated with any file(s)
        representing the dataset, during a 'training' session. If any of the
        file(s) fails validation, this method will return False. Otherwise,
        the method will return a list of unique 'file upload(s)', discarding
        duplicates.

        '''

        # local variables
        list_error = []

        dataset = self.svm_data['data']['dataset']
        acceptable_type = ['csv', 'xml', 'json']

        unique_hash = set()
        dataset_keep = []

        if (dataset.get('file_upload', None)):

            for index, filedata in enumerate(dataset['file_upload']):
                try:
                    split_path = os.path.splitext(filedata['filename'])
                    filehash = calculate_md5(filedata['file'])
                    # add 'hashed' value of file reference(s) to a list
                    if filehash not in unique_hash:
                        unique_hash.add(filehash)
                        file_extension = split_path[1][1:].strip().lower()

                        # validate file_extension
                        if (file_extension not in acceptable_type):
                            msg = '''Problem: Uploaded file, \''''
                            msg += filedata['filename']
                            msg += '''\', must be one of the formats:'''
                            msg += '\n ' + ', '.join(acceptable_type)
                            list_error.append(msg)

                        # keep non-duplicated file uploads
                        else:
                            dataset_keep.append({
                                'type': file_extension,
                                'file': filedata['file'],
                                'filename': filedata['filename']
                            })
                except:
                    msg = 'Problem with file upload #' + filedata['filename']
                    msg += '. Please re-upload the file.'
                    list_error.append(msg)

            # replace portion of dataset with unique 'file reference(s)'
            dataset['file_upload'][:] = dataset_keep

        else:
            msg = 'No file(s) were uploaded'
            list_error.append(msg)

        # return error
        if len(list_error) > 0:
            return {'error': list_error, 'dataset': None}
        else:
            return {'error': None, 'dataset': dataset}
