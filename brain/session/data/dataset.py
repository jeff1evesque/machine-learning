#!/usr/bin/python

'''

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.converter.dataset import Dataset


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

            for dataset in adjusted_datasets:
                # convert dataset(s)
                converter = Dataset(dataset['file'], model_type)
                if dataset['filename'].lower().endswith('.csv'):
                    converted.append(converter.csv_to_dict())
                elif dataset['filename'].lower().endswith('.json'):
                    converted = converter.json_to_dict()
                elif dataset['filename'].lower().endswith('.xml'):
                    converted = converter.xml_to_dict()

        # build new (relevant) dataset
        payload = {
            'premodel_dataset': converted,
            'settings': settings
        }

        # return results
        return {
            'dataset': payload,
            'error': None
        }

    except Exception as error:
        list_error.append(error)

        return {
            'dataset': None,
            'error': list_error
        }
