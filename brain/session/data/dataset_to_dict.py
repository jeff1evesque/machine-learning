#!/usr/bin/python

'''

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from flask import current_app
from brain.converter.convert_dataset import Convert_Dataset


def dataset_dictionary(id_entity, model_type, upload):
    '''

    This method converts the supplied csv, or xml file upload(s) to a uniform
    dict object.

    @upload, uploaded dataset(s).

    '''

    # local variables
    dataset = []
    observation_labels = []
    list_error = []
    json_upload = upload['dataset'].get('json_string', None)
    list_model_type = current_app.config.get('MODEL_TYPE')

    if json_upload:
        is_json = True
    else:
        is_json = False

    try:
        # web-interface: define flag to convert to dataset to json
        if upload['dataset']['file_upload']:
            for val in upload['dataset']['file_upload']:
                # reset file-pointer
                val['file'].seek(0)

                # initialize converter
                converter = Convert_Dataset(
                    val['file'],
                    model_type,
                    is_json
                )

                # convert dataset(s)
                if val['type'] == 'csv':
                    converted = converter.csv_to_dict()
                elif val['type'] == 'json':
                    converted = converter.json_to_dict()
                elif val['type'] == 'xml':
                    converted = converter.xml_to_dict()

                count_features = converter.get_feature_count()
                labels = converter.get_observation_labels()

                # assign observation labels
                observation_labels.append(labels)

                # build new (relevant) dataset
                dataset.append({
                    'id_entity': id_entity,
                    'premodel_dataset': converted,
                    'count_features': count_features
                })

        # programmatic-interface
        elif json_upload:
            # classification
            if upload['settings']['model_type'] == list_model_type[0]:
                for dataset_json in json_upload.items():
                    # conversion
                    converter = Convert_Dataset(dataset_json, model_type, True)
                    converted = converter.json_to_dict()
                    count_features = converter.get_feature_count()

                    observation_labels.append(str(dataset_json[0]))

                    # build new (relevant) dataset
                    dataset.append({
                        'id_entity': id_entity,
                        'premodel_dataset': converted,
                        'count_features': count_features
                    })

            # regression
            elif upload['settings']['model_type'] == list_model_type[1]:
                # conversion
                converter = Convert_Dataset(json_upload, model_type, True)
                converted = converter.json_to_dict()
                count_features = converter.get_feature_count()

                for criterion, predictors in json_upload.items():
                    observation_labels.append(criterion)

                # build new (relevant) dataset
                dataset.append({
                    'id_entity': id_entity,
                    'premodel_dataset': converted,
                    'count_features': count_features
                })

    except Exception as error:
        list_error.append(error)
        print error

    # return results
    if len(list_error) > 0:
        return {
            'dataset': dataset,
            'observation_labels': observation_labels,
            'error': list_error
        }
    else:
        return {
            'dataset': dataset,
            'observation_labels': observation_labels,
            'error': False
        }
