#!/usr/bin/python

'''@convert_upload.py

This file restructures only the supplied dataset(s).

'''

import csv
import json
import xmltodict
from itertools import islice
from brain.validator.validate_dataset import Validate_Dataset


class Convert_Upload(object):
    '''@Convert_Upload

    This class provides an interface to convert the supplied dataset(s),
    regardless of format (csv, json, xml), into a uniform dictionary object.

    Also, this class has the capacity of returning the following generalized
    attributes, that can be expected on any given observation, within the
    specified dataset:

        - observation labels: unique list of (independent variable) labels,
              expected on any given observation instance.
        - feature count: unique count of features, expected on any given
              observation instance.

    Note: this class explicitly inherits the 'new-style' class.

    '''

    def __init__(self, svm_data, is_json=False):
        '''@__init__

        This constructor is responsible for defining class variables.

        @is_json, flag indicating 'svm_data' is a json string.

        '''

        self.svm_data = svm_data
        self.is_json = is_json
        self.observation_labels = None
        self.count_features = None

    def csv_to_dict(self):
        '''@csv_to_dict

        This method converts the supplied csv file-object to a python
        dictionary.

        @list_observation_label, is a list containing dependent variable
            labels.

        Note: we use the 'Universal Newline Support' with the 'U" parameter
            when opening 'self.svm_data'. This allows newlines to be
            understood regardless, if the newline character was created in
            osx, windows, or linux.

        Note: since 'row' is a list, with one comma-delimited string element,
            the following line is required in this method:

                row = row[0].split(',')

        '''

        list_dataset = []
        list_observation_label = []
        list_feature_label = []

        # open temporary 'csvfile' reader object
        dataset_reader = csv.reader(
            self.svm_data,
            delimiter=' ',
            quotechar='|'
        )

        # iterate first row of csvfile
        for row in islice(dataset_reader, 0, 1):

            # iterate each column in a given row
            row_indep_label = row[0].split(',')
            for value in islice(row_indep_label, 1, None):
                validate = Validate_Dataset(value)
                validate.validate_label()

                list_error = validate.get_errors()
                if list_error:
                    print list_error
                    return None
                else:
                    list_feature_label.append(value)

        # iterate all rows of csvfile
        for dep_index, row in enumerate(islice(dataset_reader, 0, None)):

            # iterate first column of each row (except first)
            row_dep_label = row[0].split(',')
            for value in row_dep_label[:1]:
                validate = Validate_Dataset(value)
                validate.validate_label()

                list_error = validate.get_errors()
                if list_error:
                    print list_error
                    return None
                else:
                    list_observation_label.append(value)

            # generalized feature count in an observation
            row_indep_variable = row[0].split(',')
            if not self.count_features:
                self.count_features = len(row_indep_variable) - 1

            # iterate each column in a given row
            for indep_index, value in enumerate(
                islice(row_indep_variable, 1, None)
            ):

                try:
                    validate = Validate_Dataset(value)
                    validate.validate_value()

                    list_error = validate.get_errors()
                    if list_error:
                        print list_error
                        return None
                    else:
                        value = float(value)
                except Exception as error:
                    print error
                    return False

                list_dataset.append({
                    'dep_variable_label': list_observation_label[dep_index],
                    'indep_variable_label': list_feature_label[indep_index],
                    'indep_variable_value': value
                })

        # close file, save observation labels, and return
        self.svm_data.close()
        self.observation_labels = list_observation_label
        return list_dataset

    def json_to_dict(self):
        '''@json_to_dict

        This method converts the supplied json file-object to a python
        dictionary.

        @list_observation_label, is a list containing dependent variable
            labels.

        '''

        list_dataset = []
        observation_labels = []

        if self.is_json:
            dataset = self.svm_data
        else:
            dataset = json.load(self.svm_data)

        for observation_label in dataset:
            # variables
            observations = dataset[observation_label]

            # dependent variable with single observation
            if type(observations) == list:
                for observation in observations:
                    for feature_label, feature_value in observation.items():
                        list_dataset.append({
                            'dep_variable_label': observation_label,
                            'indep_variable_label': feature_label,
                            'indep_variable_value': feature_value
                        })

                    # generalized feature count in an observation
                    if not self.count_features:
                        self.count_features = len(observation)

            # dependent variable with multiple observations
            elif type(observations) == dict:
                for feature_label, feature_value in observations.items():
                    list_dataset.append({
                        'dep_variable_label': observation_label,
                        'indep_variable_label': feature_label,
                        'indep_variable_value': feature_value
                    })

                # generalized feature count in an observation
                if not self.count_features:
                    self.count_features = len(observations)

            # list of observation label
            observation_labels.append(observation_label)

        # close file
        if not self.is_json:
            self.svm_data.close()

        # save observation labels, and return
        self.observation_labels = observation_labels
        return list_dataset

    def xml_to_dict(self):
        '''@xml_to_dict

        This method converts the supplied xml file-object to a python
        dictionary.

        @list_observation_label, is a list containing dependent variable
            labels.

        '''

        list_dataset = []
        list_observation_label = []

        # convert xml file to python 'dict'
        dataset = xmltodict.parse(self.svm_data)

        # build 'list_dataset'
        for observation in dataset['dataset']['observation']:
            observation_label = observation['dependent-variable']

            validate = Validate_Dataset(observation_label)
            validate.validate_label()

            list_error = validate.get_errors()
            if list_error:
                print list_error
                return None
            else:
                list_observation_label.append(observation_label)

            for feature in observation['independent-variable']:
                feature_label = feature['label']
                feature_value = feature['value']

                validate_label = Validate_Dataset(feature_label)
                validate_value = Validate_Dataset(feature_value)

                validate_label.validate_label()
                validate_value.validate_value()

                list_error_label = validate.get_errors()
                list_error_value = validate.get_errors()
                if list_error_label or list_error_value:
                    print list_error_label
                    print list_error_value
                    return None
                else:
                    list_dataset.append({
                        'dep_variable_label': observation_label,
                        'indep_variable_label': feature_label,
                        'indep_variable_value': feature_value
                    })

            # generalized feature count in an observation
            if not self.count_features:
                self.count_features = len(observation['independent-variable'])

        # close file, save observation labels, and return
        self.svm_data.close()
        self.observation_labels = list_observation_label
        return list_dataset

    def get_observation_labels(self):
        '''@get_observation_labels

        This method returns a unique list of (independent variable) labels
        that can be expected on any given observation instance. Since both
        'csv_to_dict', and 'xml_to_dict' defines the class variable this
        method returns, either method needs to be called before this one.

        '''

        return self.observation_labels

    def get_feature_count(self):
        '''@get_feature_count

        This method returns the unique count of features that can be expected
        on any given observation instance.

        '''

        return self.count_features
