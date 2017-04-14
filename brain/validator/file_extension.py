#!/usr/bin/python

'''

This script performs validation on the file extension for file upload(s), and
returns the validated temporary file references(s), along with the
corresponding file extension for each file upload(s).

'''

import os.path
import urllib
import cStringIO
from brain.converter.md5 import calculate


class Validator(object):
    '''

    This class provides an interface to validate the file extension,
    associated with any file(s) representing the dataset.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, premodel_data, session_type=None):
        '''

        This constructor saves a subset of the passed-in form data.

        '''

        self.premodel_data = premodel_data
        self.session_type = session_type

    def validate(self):
        '''

        This method validates the file extension, associated with any file(s)
        representing the dataset, during a 'training' session. If any of the
        file(s) fails validation, this method will return False. Otherwise,
        the method will return a list of unique 'file upload(s)', discarding
        duplicates.

        '''

        # local variables
        list_error = []
        acceptable_type = ['csv', 'xml', 'json']

        unique_data = set()
        dataset_keep = []

        # validate and restructure: file upload
        if (
                self.premodel_data['data'].get('settings', None) and
                self.premodel_data['data']['settings'].get(
                    'dataset_type', None) == 'file_upload' and
                self.premodel_data.get('data', None) and
                self.premodel_data['data'].get('dataset', None) and
                self.premodel_data['data']['dataset'].get('file_upload', None)
        ):

            dataset = self.premodel_data['data']['dataset']

            for index, filedata in enumerate(dataset['file_upload']):
                try:
                    split_path = os.path.splitext(filedata['filename'])
                    filehash = calculate(filedata['file'])
                    # add 'hashed' value of file reference(s) to a list
                    if filehash not in unique_data:
                        unique_data.add(filehash)
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

        # validate and restructure: url reference
        elif (
                self.premodel_data.get('data', None) and
                self.premodel_data['data'].get('dataset', None) and
                self.premodel_data['data']['dataset'].get(
                    'type', None) and
                self.premodel_data['data']['dataset']['type'] == 'dataset_url'
        ):

            dataset = self.premodel_data['data']['dataset']
            urls = self.premodel_data['data']['dataset']['file_upload']

            for index, url in enumerate(urls):
                split_path = os.path.splitext(url)
                file_extension = split_path[1][1:].strip().lower()

                try:
                    if url not in unique_data:
                        unique_data.add(url)

                        # validate file_extension
                        if (file_extension not in acceptable_type):
                            msg = '''Problem: url reference, \''''
                            msg += file_extension
                            msg += '''\', must be one of the formats:'''
                            msg += '\n ' + ', '.join(acceptable_type)
                            list_error.append(msg)

                        # keep non-duplicated url references
                        else:
                            filename = os.path.split(url)[1]
                            dataset_keep.append({
                                'type': file_extension,
                                'file': cStringIO.StringIO(
                                            urllib.urlopen(url).read()
                                        ),
                                'filename': filename
                            })

                except:
                    msg = 'Problem with url reference ' + url
                    msg += '. Please re-upload the information.'
                    list_error.append(msg)

            # define unique 'file reference(s)'
            dataset['file_upload'][:] = dataset_keep

        else:
            msg = 'No file(s) were uploaded'
            list_error.append(msg)

        # return error
        if len(list_error) > 0:
            return {'error': list_error, 'dataset': None}
        else:
            return {'error': None, 'dataset': dataset}
