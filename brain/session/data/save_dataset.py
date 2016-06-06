#!/usr/bin/python

'''@save_dataset

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.database.save_feature import Save_Feature


def dataset(dataset):
    '''@dataset

    This method saves each dataset element (independent variable value) into
    the sql database.

    '''

    # variables
    list_error = []

    # save dataset
    for data in dataset:
        for dataset in data['premodel_dataset']:
            db_save = Save_Feature({
                'premodel_dataset': dataset,
                'id_entity': data['id_entity']
            })

            # save dataset element, append error(s)
            db_return = db_save.save_feature()
            if db_return['error']:
                list_error.append(db_return['error'])

    # return
    return {'error': list_error}
