#!/usr/bin/python

'''

This file restructures only the supplied dataset(s), from a json file to a
python dictionary format.

'''

import json


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

    # web-interface
    if not is_json:
        dataset = json.load(raw_data)

        for criterion, predictors in dataset.items():
            observation_label = criterion

            # list of observation label
            observation_labels.append(criterion)

            # criterion with single observation
            if type(predictors) == dict:

                # generalized feature count in an observation
                if not feature_count:
                    feature_count = len(predictors)

            # criterion with multiple observation
            if type(predictors) == list:

                # generalized feature count in an observation
                if not feature_count:
                    feature_count = len(predictors[0].items())

    # programmatic-interface
    else:
        dataset = raw_data

        for criterion, predictors in dataset.items():
            # list of observation label
            observation_labels.append(criterion)

            # criterion with single observation
            if type(predictors) == dict:

                # generalized feature count in an observation
                if not feature_count:
                    feature_count = len(predictors.items())

            # criterion with multiple observation
            if type(predictors) == list:

                # generalized feature count in an observation
                if not feature_count:
                    feature_count = len(predictors[0].items())

    # close file
    if not is_json:
        raw_data.close()

    # save observation labels, and return
    return {
        'dataset': list_dataset,
        'observation_labels': observation_labels,
        'feature_count': feature_count
    }
