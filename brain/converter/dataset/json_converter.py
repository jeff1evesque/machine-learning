#!/usr/bin/python

'''@json_converter.py

This file restructures only the supplied dataset(s), from a json file to a
python dictionary format.

'''

import json
from brain.validator.validate_dataset import Validate_Dataset


def svm_json_converter(raw_data, is_json):
    '''@svm_json_converter

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
    self.logger = Logger(__name__, 'error', 'error')

    if is_json:
        dataset = raw_data
    else:
        dataset = json.load(raw_data)

    for observation_label in dataset:
        # variables
        observations = dataset[observation_label]

        # validation (part 1)
        validate_olabel = Validate_Dataset(observation_label)
        validate_olabel.validate_label()

        # dependent variable with single observation
        if type(observations) == list:
            for observation in observations:
                for feature_label, feature_value in observation.items():
                    # validation (part 2)
                    validate_flabel = Validate_Dataset(feature_label)
                    validate_flabel.validate_label()
                    validate_fvalue = Validate_Dataset(feature_value)
                    validate_fvalue.validate_value()

                    # restructured data
                    list_dataset.append({
                        'dep_variable_label': observation_label,
                        'indep_variable_label': feature_label,
                        'indep_variable_value': feature_value
                    })

                # generalized feature count in an observation
                if not feature_count:
                    feature_count = len(observation)

        # dependent variable with multiple observations
        elif type(observations) == dict:
            for feature_label, feature_value in observations.items():
                # validation (part 2)
                validate_flabel = Validate_Dataset(feature_label)
                validate_flabel.validate_label()
                validate_fvalue = Validate_Dataset(feature_value)
                validate_fvalue.validate_value()

                # restructured data
                list_dataset.append({
                    'dep_variable_label': observation_label,
                    'indep_variable_label': feature_label,
                    'indep_variable_value': feature_value
                })

            # generalized feature count in an observation
            if not feature_count:
                feature_count = len(observations)

        # list of observation label
        observation_labels.append(observation_label)

        # check for errors
        olabel_error = validate_olabel.get_errors()
        flabel_error = validate_flabel.get_errors()
        fvalue_error = validate_fvalue.get_errors()
        for error in [olabel_error, flabel_error, fvalue_error]:
            if error:
                self.logger.log(error)
        if len(error) > 0:
            return None

    # close file
    if not is_json:
        raw_data.close()

    # save observation labels, and return
    return {
        'dataset': list_dataset,
        'observation_labels': observation_labels,
        'feature_count': feature_count
    }
