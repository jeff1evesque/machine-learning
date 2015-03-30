#!/usr/bin/python

## @convert_upload.py
#  This file contains methods required to convert an svm dataset, into a
#      python dictionary.
import csv
import json
import xmltodict
from collections import defaultdict
from itertools import islice
from brain.validator.validate_dataset import Validate_Dataset

## Class: Convert_Upload, explicitly inherit 'new-style' class.
#
#  Note: this class is invoked within 'base_data.py'
class Convert_Upload(object):

    ## constructor
    def __init__(self, svm_file):
        self.svm_file           = svm_file
        self.observation_labels = None
        self.count_features     = None

    ## csv_to_dict: convert csv file-object to a python dictionary.
    #
    #  @observation_label, is a list containing dependent variable labels.
    #
    #  Note: we use the 'Universal Newline Support' with the 'U" parameter
    #        when opening 'self.svm_file'. This allows newlines to be
    #        understood regardless, if the newline character was created in
    #        osx, windows, or linux.
    #
    #  Note: since 'row' is a list, with one comma-delimited string element,
    #        the following line is required in this method:
    #
    #            row = row[0].split(',')
    def csv_to_dict(self):
        list_dataset         = []
        observation_label    = []
        indep_variable_label = []

        # open temporary 'csvfile' reader object
        dataset_reader = csv.reader(self.svm_file, delimiter=' ', quotechar='|')

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
                    indep_variable_label.append(value)

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
                    observation_label.append(value)

            # generalized feature count in an observation
            row_indep_variable = row[0].split(',')
            if not self.count_features:
                self.count_features = len(row_indep_variable) - 1

            # iterate each column in a given row
            for indep_index, value in enumerate(islice(row_indep_variable, 1, None)):
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

                list_dataset.append({'dep_variable_label': observation_label[dep_index], 'indep_variable_label': indep_variable_label[indep_index], 'indep_variable_value': value})

        self.observation_labels = observation_label

        # close file, and return
        self.svm_file.close()
        return list_dataset

    ## json_to_dict: convert json file-object to a python dictionary.
    def json_to_dict(self):
        list_dataset      = []
        observation_label = []
        dataset           = json.load(self.svm_file)

        for dep_variable in dataset:
            if type(dataset[dep_variable]) == list:
                for observation in dataset[dep_variable]:
                    for indep_variable_label, indep_variable_value in observation.items():
                        list_dataset.append({'dep_variable_label': dep_variable, 'indep_variable_label': indep_variable_label, 'indep_variable_value': indep_variable_value})
            elif type(dataset[dep_variable]) == dict:
                for indep_variable_label, indep_variable_value in dataset[dep_variable].items():
                    list_dataset.append({'dep_variable_label': dep_variable, 'indep_variable_label': indep_variable_label, 'indep_variable_value': indep_variable_value})

            # list of observation label
            observation_label.append(dep_variable)

            # generalized feature count in an observation
            if not self.count_features:
                self.count_features = len(dataset[dep_variable])

        self.svm_file.close()
        self.observation_labels = observation_label

        return list_dataset

    ## xml_to_dict: convert xml file-object to a python dictionary.
    #
    #  @observation_label, is a list containing dependent variable labels.
    def xml_to_dict(self):
        list_dataset      = []
        observation_label = []

        # convert xml file to python 'dict'
        dataset = xmltodict.parse(self.svm_file)

        # build 'list_dataset'
        for dep_variable in dataset['dataset']['entity']:
            dep_variable_label = dep_variable['dependent-variable']

            validate = Validate_Dataset(dep_variable_label)
            validate.validate_label()

            list_error = validate.get_errors()
            if list_error:
                print list_error
                return None
            else:
                observation_label.append(dep_variable_label)

            for indep_variable in dep_variable['independent-variable']:
                indep_variable_label = indep_variable['label']
                indep_variable_value = indep_variable['value']

                validate_label = Validate_Dataset(indep_variable_label)
                validate_value = Validate_Dataset(indep_variable_value)

                validate_label.validate_label()
                validate_value.validate_value()

                list_error_label = validate.get_errors()
                list_error_value = validate.get_errors()
                if list_error_label or list_error_value:
                    print list_error_label
                    print list_error_value
                    return None
                else:
                    list_dataset.append({'dep_variable_label': dep_variable_label, 'indep_variable_label': indep_variable_label, 'indep_variable_value': indep_variable_value})

            # generalized feature count in an observation
            if not self.count_features:
                self.count_features = len(dep_variable['independent-variable'])

        self.observation_labels = observation_label

        # close file, and return
        self.svm_file.close()
        return list_dataset

    ## get_observation_labels: returns a list of independent variable labels. Since
    #                          both 'csv_to_dict', and 'xml_to_dict' defines the
    #                          class variable this method returns, either method
    #                          needs to be called before this one.
    def get_observation_labels(self):
        return self.observation_labels

    ## get_feature_count: return the generalied feature count for an observation
    def get_feature_count(self):
        return self.count_features
