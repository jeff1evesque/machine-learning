#!/usr/bin/python

'''

This file restructures the supplied settings, required to generate, or operate
on an existing model. The dataset is left untouched, and formatted within
'dataset.py'.

'''
from log.logger import Logger

class Settings(object):
    '''

    This class provides an interface to restructure the supplied data into a
    consistent structure, which allows successive parsers to implement
    corresponding logic.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, settings, dataset=None):
        '''

        This constructor is responsible for defining class variables.

        '''

        self.settings = settings
        self.dataset = dataset
        self.list_error = []

        self.type_web = "<class 'werkzeug.datastructures.ImmutableMultiDict'>"
        self.type_programmatic = "<type 'dict'>"

    def restructure(self):
        '''

        This method restructures the supplied data, into a consistent
        dictionary format. The nested supplied dataset, is left untouched.

        '''

        # local variables
        formatted_settings = {}
        formatted_files = []
        logger = Logger(__name__, 'error', 'error')

        # restructure settings
        try:
            logger.log('/brain/converter/settings.py, self.settings.items(): ' + repr(self.settings.items()))
            for key, value in self.settings.items():
                # web-interface: 'isinstance' did not work
                if str(type(self.settings)) == self.type_web:
                    formatted_settings['stream'] = False
                    for lvalue in self.settings.getlist(key):
                        # base case
                        if key.lower() not in formatted_settings:
                            formatted_settings[key.lower()] = lvalue.lower()
                        else:
                            # step case 1
                            if type(formatted_settings[key.lower()]) == \
                                    unicode:
                                formatted_settings[key.lower()] = [
                                    formatted_settings[key.lower()]
                                ]
                                formatted_settings[key.lower()].append(lvalue)
                            # step case n
                            elif type(formatted_settings[key.lower()]) == list:
                                formatted_settings[key.lower()].append(lvalue)

                # programmatic-interface: 'isinstance' did not work
                elif str(type(self.settings)) == self.type_programmatic:
                    formatted_settings = self.settings

        except Exception as error:
            logger.log('/brain/converter/settings.py, error: ' + repr(error))
            self.list_error.append(error)
            return {'properties': None, 'dataset': None, 'error': self.list_error}

        # restructure dataset: web-interface, dataset_url case
        if (
                self.settings and
                self.settings['dataset[]'] and
                self.settings['dataset_type'] == 'dataset_url'
           ):

            logger.log("/brain/converter/settings.py, self.dataset.getlist('dataset[]'): " + repr(self.dataset.getlist('dataset[]')))
            try:
                dataset = {
                    'upload_quantity': len(self.dataset.getlist('dataset[]')),
                    'dataset_url': self.dataset.getlist('dataset[]')
                }

            except Exception as error:
                self.list_error.append(error)
                return {'properties': None, 'dataset': None, 'error': self.list_error}

            logger.log('/brain/converter/settings.py, dataset_url (2): ' + repr(dataset))

        # restructure dataset: not all sessions involve files
        elif self.dataset:
            logger.log('/brain/converter/settings.py, self.dataset: ' + repr(self.dataset))
            try:
                # web-interface: 'isinstance' did not work
                if str(type(self.settings)) == self.type_web:
                    for file in self.dataset.getlist('dataset[]'):
                        formatted_files.append({
                            'filename': file.filename,
                            'file': file
                        })

                    dataset = {
                        'upload_quantity':
                            len(self.dataset.getlist('dataset[]')),
                        'file_upload': formatted_files
                    }

                # programmatic-interface: 'isinstance' did not work
                elif str(type(self.settings)) == self.type_programmatic:
                    dataset = self.dataset

            except Exception as error:
                self.list_error.append(error)
                return {'properties': None, 'dataset': None, 'error': self.list_error}

        else:
            dataset = None

        # return new structured data
        return {'properties': formatted_settings, 'dataset': dataset, 'error': None}

    def get_errors(self):
        '''

        This method returns all errors pertaining to the instantiated class.

        '''

        if len(self.list_error) > 0:
            return {'error': self.list_error}
        else:
            return {'error': None}
