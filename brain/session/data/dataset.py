#!/usr/bin/python

'''

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

import magic
from flask import current_app
from brain.converter.dataset import Dataset


def dataset2dict(id_entity, model_type, upload):
    '''

    This method converts the supplied csv, or xml file upload(s) to a uniform
    dict object, using necessary converter utility functions.

    @upload, uploaded dataset(s).

    '''

    # local variables
    list_error = []
    converted = []
    payload = None
    datasets = upload['datasets']
    settings = upload['properties']
    dataset_type = settings.get('dataset_type', None)
    list_model_type = current_app.config.get('MODEL_TYPE')
    f = magic.Magic(mime=True, uncompress=True)

    try:
        if dataset_type == 'file_upload':
            for val in datasets:
                # reset file-pointer
                val.seek(0)

                # initialize converter
                converter = Dataset(val, model_type)

                # convert dataset(s)
                if f.from_file(val) == 'text/plain':
                    try:
                        converted.append(converter.json_to_dict())
                    except Exception:
                        pass

                    try:
                        converted.append(converter.csv_to_dict())
                    except Exception:
                        pass

                elif f.from_file(val) == 'application/xml':
                    converted.append(converter.xml_to_dict())

            # build new (relevant) dataset
            payload = {
                'id_entity': id_entity,
                'premodel_dataset': converted,
                'settings': settings
            }

        elif dataset_type == 'dataset_url':
            # classification
            if settings['model_type'] == list_model_type[0]:
                # conversion
                converter = Dataset(dataset, model_type)
                converted.append(converter.json_to_dict())

                # build new (relevant) dataset
                payload = {
                    'id_entity': id_entity,
                    'premodel_dataset': converted,
                    'settings': settings
                }

            # regression
            elif settings['model_type'] == list_model_type[1]:
                # conversion
                converter = Dataset(json_upload, model_type)
                converted.append(converter.json_to_dict())

                # build new (relevant) dataset
                payload = {
                    'id_entity': id_entity,
                    'premodel_dataset': converted,
                    'settings': settings
                }

    except Exception as error:
        list_error.append(error)
        print error

    # return results
    if len(list_error) > 0:
        return {
            'dataset': payload,
            'error': list_error
        }
    else:
        return {
            'dataset': payload,
            'error': False
        }
