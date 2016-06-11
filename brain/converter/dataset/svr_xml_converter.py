#!/usr/bin/python

'''@svr_xml_converter.py

This file restructures only the supplied dataset(s), from an xml file to a
python dictionary format.

'''

import xmltodict
from brain.validator.validate_dataset import Validate_Dataset
from log.logger import Logger


def svr_xml_converter(raw_data):
    '''@svr_xml_converter

    This method converts the supplied xml file-object to a python dictionary.

    @raw_data, generally a file (or json string) containing the raw dataset(s),
        to be used when computing a corresponding model. If this argument is a
        file, it needs to be closed.

    @list_observation_label, is a list containing dependent variable
        labels.

    '''

    feature_count = None
    list_dataset = []
    list_observation_label = []
    logger = Logger(__name__, 'error', 'error')

    # convert xml file to python 'dict'
    dataset = xmltodict.parse(raw_data)
