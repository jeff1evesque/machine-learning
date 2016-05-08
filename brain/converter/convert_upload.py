#!/usr/bin/python

'''@convert_upload.py

This file restructures only the supplied dataset(s).

'''

import csv
import json
import xmltodict
from itertools import islice
from brain.validator.validate_dataset import Validate_Dataset
from brain.converter.dataset.csv import svm_csv_converter
from brain.converter.dataset.json import svm_json_converter


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

    def __init__(self, raw_data, is_json=False):
        '''@__init__

        This constructor is responsible for defining class variables.

        @raw_data, generally a file (or json string) containing the raw
            dataset(s), to be used when computing a corresponding model. If
            this argument is a file, it needs to be closed.

        @is_json, flag indicating 'raw_data' is a json string.

        '''

        self.raw_data = raw_data
        self.is_json = is_json
        self.observation_labels = None
        self.count_features = None

    def csv_to_dict(self):
        '''@csv_to_dict

        This method converts the supplied csv file-object to a python
        dictionary.

        @self.observation_label, is a list containing dependent variable labels.

        '''

        # svm dataset
        data = svm_csv_converter(self.raw.data)
        self.observation_labels = data['observation_labels']
        self.count_features = data['feature_count']

        return data['dataset']

    def json_to_dict(self):
        '''@json_to_dict

        This method converts the supplied json file-object to a python
        dictionary.

        @self.observation_label, is a list containing dependent variable labels.

        '''

        # svm dataset
        data = svm_json_converter(self.raw.data, self.is_json)
        self.observation_labels = data['observation_labels']
        self.count_features = data['feature_count']

        return data['dataset']

    def xml_to_dict(self):
        '''@xml_to_dict

        This method converts the supplied xml file-object to a python
        dictionary.

        @self.observation_label, is a list containing dependent variable labels.

        '''

        list_dataset = []
        list_observation_label = []

        # convert xml file to python 'dict'
        dataset = xmltodict.parse(self.raw_data)

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
        self.raw_data.close()
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
