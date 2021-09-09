#!/usr/bin/python

'''

This file restructures the supplied settings, required to generate, or operate
on an existing model. The dataset is left untouched, and formatted within
'dataset.py'.

'''


class Settings:
    '''

    This class provides an interface to restructure the supplied data into a
    consistent structure, which allows successive parsers to implement
    corresponding logic.

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
        formatted_urls = []

        # restructure settings
        try:
            for key, value in self.settings.items():
                # web-interface: 'isinstance' did not work
                if str(type(self.settings)) == self.type_web:
                    formatted_settings['stream'] = 'False'
                    for lvalue in self.settings.getlist(key):
                        # special case: this edge case, restructures the dataset, not
                        #               the settings. This is done to optimize computing,
                        #               instead of duplicating computing time below.
                        #
                        # Note: the dataset is provided with the settings, since 'url'
                        #       input types are not considered file objects during form
                        #       submission, from the web-interface.
                        #
                        if key.lower() == 'dataset[]':
                            formatted_urls.append(lvalue)

                        # base case
                        elif key.lower() not in formatted_settings:
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
            self.list_error.append(error)
            return {'properties': None, 'dataset': None, 'error': self.list_error}

        # restructure dataset: premised on above 'special case'
        if formatted_urls:
            dataset = {
                'upload_quantity': len(formatted_urls),
                'dataset_url': formatted_urls
            }

        # restructure dataset: remaining cases
        elif self.dataset:
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
