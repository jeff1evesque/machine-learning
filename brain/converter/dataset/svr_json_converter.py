#!/usr/bin/python

'''@svr_json_converter.py

This file restructures only the supplied dataset(s), from a json file to a
python dictionary format.

'''

import json
from brain.validator.validate_dataset import Validate_Dataset
from log.logger import Logger


def svr_json_converter(raw_data, is_json):
    '''@svr_json_converter

    This method converts the supplied json file-object to a python
    dictionary.

    @raw_data, generally a file (or json string) containing the raw dataset(s),
        to be used when computing a corresponding model. If this argument is a
        file, it needs to be closed.

    @is_json, flag indicating 'raw_data' is a json string.

    @observation_labels, is a list containing dependent variable labels.

    '''

    feature_count = None
    list_dataset = []
    observation_labels = []
    logger = Logger(__name__, 'error', 'error')

    if is_json:
        dataset = raw_data
    else:
        dataset = json.load(raw_data)
