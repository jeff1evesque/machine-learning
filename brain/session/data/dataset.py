#!/usr/bin/python

'''

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

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
    datasets = upload['datasets']
    settings = upload['properties']
    stream = settings.get('stream', None)

    try:
        # programmatic-interface
        if settings['stream']:
            converter = Dataset(datasets, model_type)
            converted.append(converter.json_to_dict())

        # web-interface
        else:
            for val in datasets:
                # reset file-pointer
                val['file'].seek(0)

                # convert dataset(s)
                converter = Dataset(val['file'], model_type)
                if val['type'] == 'csv':
                    converted.append(converter.csv_to_dict())
                elif val['type'] == 'json':
                    converted = converter.json_to_dict()
                elif val['type'] == 'xml':
                    converted = converter.xml_to_dict()

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
