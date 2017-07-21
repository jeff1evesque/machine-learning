#!/usr/bin/python

'''

This file restructures only the supplied dataset(s), from a csv file to a
python dictionary format.

'''

import csv
from itertools import islice
from brain.validator.dataset import Validator
from log.logger import Logger


def svm_csv2dict(raw_data):
    '''

    This method converts the supplied csv file-object, intended for an svm
    model, to a python dictionary.

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

    dataset = []
    logger = Logger(__name__, 'error', 'error')

    # open temporary 'csvfile' reader object
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
        features_dict = {k: v for k, v in zip(indep_labels_list, features_list)}

        observation = {
            'dependent-variable': row_arr[:1][0],
            'independent-variables': [features_dict]
        }

        dataset.append(observation)

    logger.log('/brain/converter/svm/csvtodict.py, dataset: ' + repr(dataset))
    # close file, return dataset
    raw_data.close()
    return dataset
