#!/usr/bin/python

'''

This file restructures only the supplied dataset(s), from a csv file to a
python dictionary format.

'''

import csv
from itertools import islice
from brain.validator.validate_dataset import Validate_Dataset
from log.logger import Logger


def svm_csv_converter(raw_data):
    '''

    This method converts the supplied csv file-object, intended for an svm
    model, to a python dictionary.

    @raw_data, generally a file (or json string) containing the raw dataset(s),
        to be used when computing a corresponding model. If this argument is a
        file, it needs to be closed.

    @list_observation_label, is a list containing dependent variable labels.

    Note: we use the 'Universal Newline Support' with the 'U' parameter when
          opening 'raw_data'. This allows newlines to be understood regardless,
          if the newline character was created in osx, windows, or linux.

    Note: since 'row' is a list, with one comma-delimited string element, the
          following line is required in this method:

          row = row[0].split(',')

        '''

    feature_count = None
    list_dataset = []
    list_observation_label = []
    list_feature_label = []
    logger = Logger(__name__, 'error', 'error')

    # open temporary 'csvfile' reader object
    dataset_reader = csv.reader(
        raw_data,
        delimiter=' ',
        quotechar='|'
    )

    # iterate first row of csvfile
    for row in islice(dataset_reader, 0, 1):

        # iterate each column in a given row
        row_indep_label = row[0].split(',')
        for value in islice(row_indep_label, 1, None):
            list_feature_label.append(str(value))

    # iterate all rows of csvfile
    for dep_index, row in enumerate(islice(dataset_reader, 0, None)):

        # iterate first column of each row (except first)
        row_dep_label = row[0].split(',')
        for value in row_dep_label[:1]:
            list_observation_label.append(str(value))

        # generalized feature count in an observation
        row_indep_variable = row[0].split(',')
        if not feature_count:
            feature_count = len(row_indep_variable) - 1

        # iterate each column in a given row
        for indep_index, value in enumerate(
            islice(row_indep_variable, 1, None)
        ):

            try:
                validate = Validate_Dataset(value)
                validate.validate_value()

                list_error = validate.get_errors()
                if list_error:
                    logger.log(list_error)
                    return None
                else:
                    value = float(value)
            except Exception as error:
                logger.log(error)
                return False

            list_dataset.append({
                'dep_variable_label': list_observation_label[dep_index],
                'indep_variable_label': list_feature_label[indep_index],
                'indep_variable_value': value
            })

    # close file, save observation labels, and return
    raw_data.close()
    return {
        'dataset': list_dataset,
        'observation_labels': list_observation_label,
        'feature_count': feature_count
    }
