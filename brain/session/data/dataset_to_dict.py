#!/usr/bin/python

'''@save_entity

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

'''

from brain.converter.convert_dataset import Convert_Dataset


def dataset_dictionary(id_entity, model_type, upload):
    '''@dataset_dictionary

    This method converts the supplied csv, or xml file upload(s) to a uniform
    dict object.

    @flag_append, when false, indicates the neccessary 'dataset' was not
        properly defined, causing this method to 'return', which essentially
        stops the execution of the current session.

    @upload, uploaded dataset(s).

    '''

    flag_append = True
    dataset = []
    observation_labels = []
    list_error = []

    try:
        # web-interface: define flag to convert to dataset to json
        if upload['dataset']['file_upload']:
            for val in upload['dataset']['file_upload']:
                # reset file-pointer
                val['file'].seek(0)

                # csv to dict
                if val['type'] == 'csv':
                    try:
                        # conversion
                        converter = Convert_Dataset(val['file'], model_type)
                        converted = converter.csv_to_dict()
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
                    except Exception as error:
                        list_error.append(error)
                        flag_append = False

                # json to dict
                elif val['type'] == 'json':
                    try:
                        # conversion
                        converter = Convert_Dataset(val['file'], model_type)
                        converted = converter.json_to_dict()
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
                    except Exception as error:
                        list_error.append(error)
                        flag_append = False

                # xml to dict
                elif val['type'] == 'xml':
                    try:
                        # conversion
                        converter = Convert_Dataset(val['file'], model_type)
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
                    except Exception as error:
                        list_error.append(error)
                        flag_append = False

            if not flag_append:
                return False

        # programmatic-interface
        elif upload['dataset']['json_string']:
            for dataset_json in upload['dataset']['json_string']:
                # conversion
                converter = Convert_Dataset(dataset_json, model_type, True)
                converted = converter.json_to_dict()
                count_features = converter.get_feature_count()

                observation_labels.append(str(dataset_json['criterion']))

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
    if list_error:
        return {
            'dataset': dataset,
            'observation_labels': observation_labels,
            'error': list_error
        }
    else:
        return {
            'dataset': dataset,
            'observation_labels': observation_labels,
            'error': None
        }
