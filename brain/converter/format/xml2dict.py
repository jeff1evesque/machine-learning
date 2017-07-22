#!/usr/bin/python

'''

This file restructures only the supplied dataset(s), from an xml file to a
python dictionary format.

'''

import xmltodict
from brain.validator.dataset import Validator
from log.logger import Logger


def xml2dict(raw_data):
    '''

    This method converts the supplied xml file-object to a python dictionary.

    @raw_data, generally a file (or json string) containing the raw dataset(s),
        to be used when computing a corresponding model. If this argument is a
        file, it needs to be closed.

    '''

    # convert xml file to python 'dict'
    dataset = []
    dataset_reader = xmltodict.parse(raw_data)

    # build 'list_dataset'
    for observation in dataset_reader['dataset']['observation']:
        features_dict = {}
        dependent_variable = observation['dependent-variable']

        for feature in observation['independent-variable']:
            features_dict[feature['feature_label']] = feature['value']

        observation = {
            'dependent-variable': dependent_variable,
            'independent-variables': [features_dict]
        }

        dataset.append(observation)

    logger = Logger(__name__, 'error', 'error')
    logger.log('/brain/converter/format/xml2dict.py, dataset: ' + repr(dataset))

    # save observation labels, and return
    raw_data.close()
    return dataset
