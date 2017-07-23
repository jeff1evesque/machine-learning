#!/usr/bin/python

'''

This file restructures only the supplied dataset(s), from a csv file to a
python dictionary format.

'''

import csv
from itertools import islice
from brain.validator.dataset import Validator


def csv2dict(raw_data):
    '''

    This method converts the supplied csv file-object to a python dictionary.

    @raw_data, generally a file (or json string) containing the raw dataset(s),
        to be used when computing a corresponding model. If this argument is a
        file, it needs to be closed.

    Note: we use the 'Universal Newline Support' with the 'U' parameter when
          opening 'raw_data'. This allows newlines to be understood regardless,
          if the newline character was created in osx, windows, or linux.

    Note: since 'row' is a list, with one comma-delimited string element, the
          following line is required in this method:

          row = row[0].split(',')

    '''

    # local variables:
    dataset = []
    validate = Validator()

    # local variable: open temporary 'csvfile' reader object
    dataset_reader = csv.reader(
        raw_data,
        delimiter=' ',
        quotechar='|'
    )

    # first row of csvfile: get all columns, except first
    for row in islice(dataset_reader, 0, 1):
        indep_labels_list = row[0].split(',')[1:]

    # all rows of csvfile: except first row
    for dep_index, row in enumerate(islice(dataset_reader, 0, None)):
        row_arr = row[0].split(',')
        features_list = row_arr[1:]

        # merge lists into dict if each independent variable validates
        if all(validate.validate_value(item) for item in features_list):
            features_dict = {k: v for k, v in zip(indep_labels_list, features_list)}
            error = None
        else:
            error = 'csv conversion failed: ' + validate.get_error()

        observation = {
            'dependent-variable': row_arr[:1][0],
            'independent-variables': [features_dict],
            'error': error
        }

        dataset.append(observation)

    # close file, return dataset
    raw_data.close()
    return dataset
