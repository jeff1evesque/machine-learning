#!/usr/bin/python

'''

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

import json
import requests
from flask import current_app
from brain.validator.dataset import Validator
from brain.converter.format.csv2dict import csv2dict
from brain.converter.format.xml2dict import xml2dict


def dataset2dict(model_type, upload):
    '''

    This method converts the supplied csv, or xml file upload(s) to a uniform
    dict object, using necessary converter utility functions.

    @upload, uploaded dataset(s).

    '''

    # local variables
    list_error = []
    converted = []
    Validate = Validator()
    datasets = upload['dataset']
    settings = upload['properties']
    stream = settings.get('stream', None)
    list_model_type = current_app.config.get('MODEL_TYPE')

    # programmatic-interface
    if stream == 'True':
        session_name = settings['session_name']
        dataset_type = settings['dataset_type']

        # convert dataset(s) into extended list
        for dataset in datasets:
            # scrape url content
            if dataset_type == 'dataset_url':
                r = requests.get(dataset)
                instance = r.json()['dataset']

            else:
                instance = [dataset]

            if instance:
                if model_type == list_model_type[0]:
                    error = Validate.validate_classification(instance)

                elif model_type == list_model_type[1]:
                    error = Validate.validate_regression(instance)

                if error:
                    list_error.append({
                        'location': session_name,
                        'message': error
                    })

                converted.extend(instance)

    # web-interface
    else:
        dataset_type = settings['dataset_type']
        if dataset_type == 'file_upload':
            adjusted_datasets = upload['dataset']['file_upload']

        else:
            adjusted_datasets = upload['dataset']['dataset_url']

        # convert dataset(s) into extended list
        for dataset in adjusted_datasets:
            location = dataset['filename']

            # scrape url content
            if dataset_type == 'dataset_url':
                r = requests.get(dataset)
                instance = [r.json()][0]['dataset']

            # file content
            else:
                if dataset['filename'].lower().endswith('.csv'):
                    instance = csv2dict(dataset['file'])

                elif dataset['filename'].lower().endswith('.json'):
                    # load dataset instance
                    try:
                        instance = json.load(dataset['file'])['dataset']
                    except:
                        instance = converted.extend(dataset['file'])
                elif dataset['filename'].lower().endswith('.xml'):
                    instance = xml2dict(dataset['file'])

            if instance:
                if model_type == list_model_type[0]:
                    error = Validate.validate_classification(instance)

                elif model_type == list_model_type[1]:
                    error = Validate.validate_regression(instance)

                if error:
                    list_error.append({
                        'location': location,
                        'message': error
                    })
                else:
                    converted.extend(instance)

            else:
                list_error.append({
                    'location': location,
                    'message': 'empty dataset, or invalid syntax (try lint)'
                })

    # return results
    if list_error:
        return {
            'dataset': converted,
            'settings': settings,
            'error': {
                'validation': list_error
            }
        }

    else:
        return {
            'dataset': converted,
            'settings': settings,
            'error': None,
        }
