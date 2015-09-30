#!/usr/bin/python

## @restructure_data.py
#  This file contains methods needed to correctly reformat input data.

## Class: Restructure_Data, explicitly inherit 'new-style class
#
#  Note: this class is invoked within 'views.py'
class Restructure_Data(object):

    ## constructor
    def __init__(self, settings, dataset=None):
        self.settings   = settings
        self.dataset    = dataset
        self.list_error = []

        self.type_web   = "<class 'werkzeug.datastructures.ImmutableMultiDict'>"
        self.type_programmatic = "<type 'dict'>"

    ## restructure: restructure input data
    def restructure(self):

        # local variables
        formatted_settings = {}
        formatted_files    = []

        # restructure settings
        try:
            for key, value in self.settings.items():
                # web-interface case: 'isinstance' implementation did not work
                if str(type(self.settings)) == self.type_web:
                    for lvalue in self.settings.getlist(key):
                        # base case
                        if key.lower() not in formatted_settings:
                            formatted_settings[key.lower()] = lvalue.lower()
                        else:
                            # step case 1
                            if type(formatted_settings[key.lower()]) == unicode:
                                formatted_settings[key.lower()] = [formatted_settings[key.lower()]]
                                formatted_settings[key.lower()].append(lvalue)
                            # step case n
                            elif type(formatted_settings[key.lower()]) == list:
                                formatted_settings[key.lower()].append(lvalue)

                # programmatic-interface case: 'isinstance' implementation did not work
                elif str(type(self.settings)) == self.type_programmatic:
                    formatted_settings = self.settings

        except Exception as error:
            self.list_error.append(error)
            return {'data': None, 'error': self.list_error}

        # restructure dataset: not all sessions involve files
        if self.dataset:
            try:
                # web-interface case: 'isinstance' implementation did not work
                if str(type(self.settings)) == self.type_web:
                    for file in self.dataset.getlist('svm_dataset[]'):
                        formatted_files.append({'filename': file.filename, 'file': file})

                    dataset = {'upload_quantity': len(self.dataset.getlist('svm_dataset[]')), 'file_upload': formatted_files, 'json_string': None}

                # programmatic-interface case: 'isinstance' implementation did not work
                elif str(type(self.settings)) == self.type_programmatic:
                    dataset = {'upload_quantity': 1, 'file_upload': None, 'json_string': self.dataset}

            except Exception as error:
                self.list_error.append(error)
                return {'data': None, 'error': self.list_error}

        else: dataset = None

        # build input structure
        data = {'settings': formatted_settings, 'dataset': dataset}
 
        # return new structured data
        return {'data': data, 'error': None}

    ## get_errors: returns all errors corresponding to this class instance
    def get_errors(self):
        if len(self.list_error) > 0: return {'error': self.list_error}
        else: return {'error': None}
