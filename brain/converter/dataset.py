#!/usr/bin/python

'''

This file restructures only the supplied dataset(s).

'''

import json
from flask import current_app
from brain.converter.svm.csv2dict import svm_csv2dict
from brain.converter.svm.xml2dict import svm_xml2dict
from brain.converter.svr.csv2dict import svr_csv2dict
from brain.converter.svr.xml2dict import svr_xml2dict


class Dataset(object):
    '''

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

    def __init__(self, raw_data, model_type):
        '''

        This constructor is responsible for defining class variables.

        @raw_data, generally a file (or json string) containing the raw
            dataset(s), to be used when computing a corresponding model. If
            this argument is a file, it needs to be closed.

        '''

        self.raw_data = raw_data
        self.model_type = model_type
        self.classification = current_app.config.get('MODEL_TYPE')[0]
        self.regression = current_app.config.get('MODEL_TYPE')[1]

    def csv_to_dict(self):
        '''

        This method converts the supplied csv file-object to a python
        dictionary.

        @self.observation_label, list containing dependent variable labels.

        '''

        # convert classification dataset
        if self.model_type == self.classification:
            data = svm_csv2dict(self.raw_data)

        # convert regression dataset
        elif self.model_type == self.regression:
            data = svr_csv2dict(self.raw_data)

        # record observation labels, and feature count
        self.observation_labels = data['observation_labels']
        self.count_features = data['feature_count']

        # return data
        return data['dataset']

    def json_to_dict(self):
        '''

        This method converts the supplied json file-object to a python
        dictionary. Otherwise, return the dictionary as is.

        '''

        try:
            dataset = json.load(self.raw_data)
        except:
            dataset = self.raw_data

        return dataset

    def xml_to_dict(self):
        '''

        This method converts the supplied xml file-object to a python
        dictionary.

        @self.observation_label, list containing dependent variable labels.

        '''

        # convert classification dataset
        if self.model_type == self.classification:
            data = svm_xml2dict(self.raw_data)

        # convert regression dataset
        elif self.model_type == self.regression:
            data = svr_xml2dict(self.raw_data)

        # record observation labels, and feature count
        self.observation_labels = data['observation_labels']
        self.count_features = data['feature_count']

        # return data
        return data['dataset']
