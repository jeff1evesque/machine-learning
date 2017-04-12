#!/usr/bin/python

'''

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.database.feature import Feature


def dataset(dataset, model_type):
    '''

    This method saves each dataset element (independent variable value) into
    the sql database.

    '''

    # variables
    list_error = []

    # save dataset
    for data in dataset:
        for select_data in data['premodel_dataset']:
            db_save = Feature({
                'premodel_dataset': select_data,
                'id_entity': data['id_entity'],
            })

            # save dataset element, append error(s)
            db_return = db_save.Feature(model_type)
            if db_return['error']:
                list_error.append(db_return['error'])

    # return
    return {'error': list_error}
