#!/usr/bin/python

'''

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.database.entity import Entity
from brain.database.feature import Feature
from brain.database.observation import Observation
from brain.validator.validate_file_extension import Validate_File_Extension


def save_info(dataset, session_type, userid):
    '''

    This method saves the current entity into the database, then returns the
    corresponding entity id.

    '''

    list_error = []
    premodel_settings = dataset['data']['settings']
    premodel_entity = {
        'title': premodel_settings.get('session_name', None),
        'uid': userid,
        'id_entity': None
    }
    db_save = Entity(premodel_entity, session_type)

    # save dataset element
    db_return = db_save.save()

    # return error(s)
    if not db_return['status']:
        list_error.append(db_return['error'])
        return {'id': None, 'error': list_error}

    # return session id
    elif db_return['status'] and session_type == 'data_new':
        return {'id': db_return['id'], 'error': None}

def save_count(dataset):
    '''

    This method saves the number of features that can be expected in a given
    observation with respect to 'id_entity'.

    @dataset, we assume that validation has occurred, and safe to assume the
        data associated with the first dataset instance is identical to any
        instance n within the overall collection of dataset(s).

    @dataset['count_features'], is defined within the 'dataset' method.

    Note: this method needs to execute after 'dataset'

    '''

    db_save = Feature({
        'id_entity': dataset['id_entity'],
        'count_features': dataset['count_features']
    })

    # save dataset element, append error(s)
    db_return = db_save.save_count()
    if db_return['error']:
        return {'error': db_return['error']}
    else:
        return {'error': None}

def save_olabels(session_type, session_id, labels, file_upload):
    '''

    This method saves the list of unique independent variable labels, which can
    be expected in any given observation, into the sql database. This list of
    labels, is predicated on a supplied session id (entity id).

    '''

    # variables
    list_error = []

    # web-interface: save labels
    if file_upload:
        if len(labels) > 0:
            for label_list in labels:
                for label in label_list:
                    db_save = Observation(
                        {
                            'label': label,
                            'id_entity': session_id
                        },
                        session_type
                    )

                    # save dataset element, append error(s)
                    db_return = db_save.save_label()
                    if not db_return['status']:
                        list_error.append(db_return['error'])

    # programmatic api: save labels
    else:
        if len(labels) > 0:
            for label in labels:
                db_save = Observation(
                    {
                        'label': label,
                        'id_entity': session_id
                    },
                    session_type
                )

                # save dataset element, append error(s)
                db_return = db_save.save_label()
                if not db_return['status']:
                    list_error.append(db_return['error'])

    # return
    return {'error': list_error}

def reduce(dataset, session_type):
    '''

    This method validates the file extension for each uploaded dataset,
    and returns the unique (non-duplicate) dataset.

    '''

    # variables
    list_error = []

    # web-interface: validate, and restructure 'file-upload' dataset
    if (
            dataset['data'].get('dataset', None) and
            dataset['data']['dataset'].get('file_upload', None) and
            dataset['data']['settings'].get(
                'dataset_type', None) == 'file_upload'
    ):

        # validate and restructure
        validator = Validate_File_Extension(
            dataset,
            session_type
        )
        adjusted_dataset = validator.validate()

        if adjusted_dataset['error']:
            list_error.append(
                adjusted_dataset['error']
            )

    # web-interface: validate, and restructure url dataset
    elif (
            dataset['data']['settings'].get('dataset[]', None) and
            dataset['data']['settings'].get(
                'dataset_type', None) == 'dataset_url'
    ):

        # define 'file_upload' since doesn't exist
        data = dataset['data']
        data['dataset'] = {}
        if type(data['settings']['dataset[]']) is list:
            data['dataset']['file_upload'] = data['settings']['dataset[]']
        else:
            data['dataset']['file_upload'] = []
            data['dataset']['file_upload'].append(
                data['settings']['dataset[]']
            )

        # validate and restructure
        validator = Validate_File_Extension(
            {
                'data': {
                    'dataset': {
                        'file_upload': data['dataset']['file_upload'],
                        'type': data['settings']['dataset_type'],
                    }
                },
            },
            session_type
        )
        adjusted_dataset = validator.validate()

        if adjusted_dataset['error']:
            list_error.append(
                adjusted_dataset['error']
            )

    # programmatic-interface: validate, do not restructure file upload
    elif (
            dataset['data']['dataset'].get('json_string', None) and
            dataset['data']['settings'].get(
                'dataset_type', None) == 'file_upload'
    ):

        adjusted_dataset = dataset['data']

        if dataset['error']:
            list_error.append(adjusted_dataset['error'])

    # programmatic-interface: validate, and restructure url dataset
    elif (
            dataset['data']['dataset'].get('json_string', None) and
            dataset['data']['settings'].get(
                'dataset_type', None) == 'dataset_url'
    ):

        # define 'file_upload' since doesn't exist
        data = dataset['data']
        if type(data['dataset']['json_string']) is list:
            data['dataset']['file_upload'] = data['dataset']['json_string']
        else:
            data['dataset']['file_upload'] = []
            data['dataset']['file_upload'].append(
                data['dataset']['json_string']
            )

        # validate and restructure
        validator = Validate_File_Extension(
            {
                'data': {
                    'dataset': {
                        'file_upload': data['dataset']['file_upload'],
                        'type': data['settings']['dataset_type'],
                    }
                },
            },
            session_type
        )
        adjusted_dataset = validator.validate()

        if adjusted_dataset['error']:
            list_error.append(
                adjusted_dataset['error']
            )

    # return
    if list_error:
        return {'dataset': None, 'error': list_error}
    else:
        return {'dataset': adjusted_dataset, 'error': None}
