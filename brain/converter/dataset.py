#!/usr/bin/python

'''

This file restructures only the supplied dataset(s).

'''

import json
from brain.converter.format.csv2dict import csv2dict
from brain.converter.format.xml2dict import xml2dict


class Dataset(object):
    '''

    This class provides an interface to convert the supplied dataset(s),
    regardless of format (csv, json, xml), into a uniform dictionary object.

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

    def csv_to_dict(self):
        '''

        This method converts the supplied csv file-object to a python
        dictionary.

        '''

        # return data
        return csv2dict(self.raw_data)

    def json_to_dict(self):
        '''

        This method converts the supplied json file-object to a python
        dictionary. Otherwise, return the dictionary as is.

        '''

        try:
            return json.load(self.raw_data)
        except:
            return self.raw_data

    def xml_to_dict(self):
        '''

        This method converts the supplied xml file-object to a python
        dictionary.

        '''

        # return data
        return xml2dict(self.raw_data)
