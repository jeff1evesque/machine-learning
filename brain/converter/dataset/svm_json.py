#!/usr/bin/python

'''

This file restructures only the supplied dataset(s), from a json file to a
python dictionary format.

'''

import json
from brain.validator.validate_dataset import Validate_Dataset
from log.logger import Logger


def svr_json2dict(raw_data, is_json):
    '''

    This method converts the supplied json file-object to a python
    dictionary.

    @raw_data, generally a file (or json string) containing the raw dataset(s),
        to be used when computing a corresponding model. If this argument is a
        file, it needs to be closed.

    @is_json, flag indicating 'raw_data' is a json string.

    @observation_labels, is a list containing dependent variable labels.

    '''

    # local variables
    feature_count = None
    list_dataset = []
    observation_labels = []
    logger = Logger(__name__, 'error', 'error')

    # web-interface
    if not is_json:
        dataset = json.load(raw_data)

        for observation_label in dataset:
            # variables
            observations = dataset[observation_label]

            # dependent variable with single observation
            if type(observations) == dict:
                for feature_label, feature_value in observations.items():
                    # validation
                    validate_fvalue = Validate_Dataset(feature_value)
                    validate_fvalue.validate_value()

                    if validate_fvalue.get_errors():
                        logger.log(validate_fvalue.get_errors())
                    else:
                        # restructured data
                        list_dataset.append({
                            'dep_variable_label': str(observation_label),
                            'indep_variable_label': str(feature_label),
                            'indep_variable_value': feature_value
                        })

                # generalized feature count in an observation
                if not feature_count:
                    feature_count = len(observations)

            # dependent variable with multiple observations
            elif type(observations) == list:
                for observation in observations:
                    for feature_label, feature_value in observation.items():
                        # validation
                        validate_fvalue = Validate_Dataset(feature_value)
                        validate_fvalue.validate_value()

                        if validate_fvalue.get_errors():
                            logger.log(validate_fvalue.get_errors())
                        else:
                            # restructured data
                            list_dataset.append({
                                'dep_variable_label': str(observation_label),
                                'indep_variable_label': str(feature_label),
                                'indep_variable_value': feature_value
                            })

                    # generalized feature count in an observation
                    if not feature_count:
                        feature_count = len(observation)

            # list of observation label
            observation_labels.append(observation_label)

    # programmatic-interface
    else:
        dataset = raw_data
        observation_label = raw_data[0]

        # list of observation label
        observation_labels.append(observation_label)

        # dependent variable with single observation
        if type(raw_data[1]) == dict:
            for label, feature in raw_data[1].items():
                # validation
                validate_fvalue = Validate_Dataset(feature)
                validate_fvalue.validate_value()

                if validate_fvalue.get_errors():
                    logger.log(validate_fvalue.get_errors())
                else:
                    # restructured data
                    list_dataset.append({
                        'dep_variable_label': str(observation_label),
                        'indep_variable_label': str(label),
                        'indep_variable_value': feature
                    })

            # generalized feature count in an observation
            if not feature_count:
                feature_count = len(raw_data[1])

        # dependent variable with multiple observations
        if type(raw_data[1]) == list:
            for feature_set in raw_data[1]:
                for feature_label, feature_value in feature_set.items():
                    # validation
                    validate_fvalue = Validate_Dataset(feature_value)
                    validate_fvalue.validate_value()

                    if validate_fvalue.get_errors():
                        logger.log(validate_fvalue.get_errors())
                    else:
                        # restructured data
                        list_dataset.append({
                            'dep_variable_label': str(observation_label),
                            'indep_variable_label': str(feature_label),
                            'indep_variable_value': feature_value
                        })

                # generalized feature count in an observation
                if not feature_count:
                    feature_count = len(feature_set)

    # close file
    if not is_json:
        raw_data.close()

    # save observation labels, and return
    return {
        'dataset': list_dataset,
        'observation_labels': observation_labels,
        'feature_count': feature_count
    }
