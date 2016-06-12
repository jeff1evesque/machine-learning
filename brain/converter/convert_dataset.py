#!/usr/bin/python

'''@convert_dataset.py

This file restructures only the supplied dataset(s).

'''

from flask import current_app
from brain.converter.dataset.svm_csv_converter import svm_csv_converter
from brain.converter.dataset.svm_json_converter import svm_json_converter
from brain.converter.dataset.svm_xml_converter import svm_xml_converter
from brain.converter.dataset.svr_csv_converter import svr_csv_converter
from brain.converter.dataset.svr_json_converter import svr_json_converter
from brain.converter.dataset.svr_xml_converter import svr_xml_converter


class Convert_Dataset(object):
    '''@Convert_Dataset

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

    def __init__(self, raw_data, model_type, is_json=False):
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
        self.model_type = model_type
        self.classication = current_app.config.get('MODEL_TYPE_CLASSICATION')

    def csv_to_dict(self):
        '''@csv_to_dict

        This method converts the supplied csv file-object to a python
        dictionary.

        @self.observation_label, list containing dependent variable labels.

        '''

        # svm dataset
        if self.model_type == self.classication:
            data = svm_csv_converter(self.raw_data)
            self.observation_labels = data['observation_labels']
            self.count_features = data['feature_count']

        return data['dataset']

    def json_to_dict(self):
        '''@json_to_dict

        This method converts the supplied json file-object to a python
        dictionary.

        @self.observation_label, list containing dependent variable labels.

        '''

        # svm dataset
        if self.model_type == self.classication:
            data = svm_json_converter(self.raw_data, self.is_json)
            self.observation_labels = data['observation_labels']
            self.count_features = data['feature_count']

        return data['dataset']

    def xml_to_dict(self):
        '''@xml_to_dict

        This method converts the supplied xml file-object to a python
        dictionary.

        @self.observation_label, list containing dependent variable labels.

        '''

        # svm dataset
        if self.model_type == self.classication:
            data = svm_xml_converter(self.raw_data)
            self.observation_labels = data['observation_labels']
            self.count_features = data['feature_count']

        return data['dataset']

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
