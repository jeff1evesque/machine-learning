#!/usr/bin/python

'''

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

import json
from flask import current_app
from jsonschema.validators import Draft4Validator
from brain.schema.dataset import svm_dataset, svr_dataset
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
    datasets = upload['dataset']
    settings = upload['properties']
    stream = settings.get('stream', None)
    list_model_type = current_app.config.get('MODEL_TYPE')

    try:
        # programmatic-interface
        if stream:
            converter = Dataset(datasets, model_type)
            converted.append(converter.json_to_dict())

        # web-interface
        else:
            if datasets.get('file_upload', None):
                adjusted_datasets = datasets['file_upload']
            else:
                adjusted_datasets = datasets['dataset_url']

            # convert dataset(s) into extended list
            for dataset in adjusted_datasets:
                if dataset['filename'].lower().endswith('.csv'):
                    converted.extend(csv2dict(dataset['file']))
                elif dataset['filename'].lower().endswith('.json'):
                    # load dataset instance
                    try:
                        instance = json.load(dataset['file'])['dataset']
                    except:
                        instance = converted.extend(dataset['file'])

                    # validate against schema, and build converted list
                    try:
                        if model_type == list_model_type[0]:
                            Draft4Validator(svm_dataset()).validate(instance)
                        elif model_type == list_model_type[1]:
                            Draft4Validator(svr_dataset()).validate(instance)
                        converted.extend(instance)
                    except Exception, error:
                        msg = "%s contains invalid syntax, with error: %s" % (
                            dataset['filename'],
                            error
                        )
                        converted.extend({'error': msg})

                elif dataset['filename'].lower().endswith('.xml'):
                    converted.extend(xml2dict(dataset['file']))

        # return results
        return {
            'dataset': converted,
            'settings': settings,
            'error': None
        }

    except Exception as error:
        list_error.append(error)

        return {
            'dataset': None,
            'error': list_error
        }
