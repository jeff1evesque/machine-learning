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

    # local variables
    feature_count = None
    list_dataset = []
    observation_labels = []
    logger = Logger(__name__, 'error', 'error')

    if is_json:
        dataset = raw_data
    else:
        dataset = json.load(raw_data)

    # web-interface
    if not is_json:
        for observation in dataset['dataset']:
            observation_label = str(observation['criterion'])

            # criterion with single observation
            if type(observation['predictors']) == dict:
                for label, predictor in observation['predictors']:
                    # validation (part 1)
                    validate_predictor = Validate_Dataset(str(predictor))
                    validate_predictor.validate_value()

                    if validate_predictor.get_errors():
                        logger.log(validate_predictor.get_errors())
                    else:
                        # restructured data
                        list_dataset.append({
                            'dep_variable_label': str(observation_label),
                            'indep_variable_label': str(label),
                            'indep_variable_value': predictor
                        })

                # generalized feature count in an observation
                if not feature_count:
                    feature_count = len(dataset['predictors'].items())

            # criterion with multiple observation
            if type(observation['predictors']) == dict:
                for criterion in observation['predictors']:
                    for label, predictor in criterion.items():
                        # validation (part 1)
                        validate_predictor = Validate_Dataset(str(predictor))
                        validate_predictor.validate_value()

                        if validate_predictor.get_errors():
                            logger.log(validate_predictor.get_errors())
                        else:
                            # restructured data
                            list_dataset.append({
                                'dep_variable_label': str(observation_label),
                                'indep_variable_label': str(label),
                                'indep_variable_value': predictor
                            })

                    # generalized feature count in an observation
                    if not feature_count:
                        feature_count = len(dataset['predictors'].items())

    # programmatic-interface
    else:
        observation_label = str(dataset['criterion'])

        # criterion with single observation
        if type(dataset['predictors']) == dict:
            for label, predictor in dataset['predictors'].items():
                # validation (part 1)
                validate_predictor = Validate_Dataset(str(predictor))
                validate_predictor.validate_value()

                if validate_predictor.get_errors():
                    logger.log(validate_predictor.get_errors())
                else:
                    # restructured data
                    list_dataset.append({
                        'dep_variable_label': str(observation_label),
                        'indep_variable_label': str(label),
                        'indep_variable_value': predictor
                    })

            # generalized feature count in an observation
            if not feature_count:
                feature_count = len(dataset['predictors'].items())

        # criterion with multiple observation
        if type(dataset['predictors']) == list:
            for criterion in dataset['predictors']:
                for label, predictor in criterion.items():
                    # validation (part 1)
                    validate_predictor = Validate_Dataset(str(predictor))
                    validate_predictor.validate_value()

                    if validate_predictor.get_errors():
                        logger.log(validate_predictor.get_errors())
                    else:
                        # restructured data
                        list_dataset.append({
                            'dep_variable_label': str(observation_label),
                            'indep_variable_label': str(label),
                            'indep_variable_value': predictor
                        })

                # generalized feature count in an observation
                if not feature_count:
                    feature_count = len(dataset['predictors'].items())

    # close file
    if not is_json:
        raw_data.close()

    # save observation labels, and return
    return {
        'dataset': list_dataset,
        'observation_labels': observation_labels,
        'feature_count': feature_count
    }
