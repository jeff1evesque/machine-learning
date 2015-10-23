#!/usr/bin/python

"""@base_data

This file serves as the superclass for 'data_xx.py' files.

Note: the term 'dataset' used throughout various comments in this file,
      synonymously implies the user supplied 'file upload(s)', and XML url
      references.

"""

from brain.database.save_entity import Save_Entity
from brain.database.save_feature import Save_Feature
from brain.validator.validate_file_extension import Validate_File_Extension
from brain.converter.convert_upload import Convert_Upload
from brain.database.save_observation import Save_Observation


class Base_Data(object):
    """@Base_Data

    This class provides an interface to save, and validate the provided
    dataset, into logical ordering within the sql database.

    @self.uid, the logged-in user (i.e. userid).

    Note: this class is invoked within 'data_xx.py'.

    Note: this class explicitly inherits the 'new-style' class.

    """

    def __init__(self, svm_data):
        """@__init__

        This constructor is responsible for defining class variables.

        """

        self.flag_upload = False
        self.observation_labels = []
        self.list_error = []
        self.uid = 1

    def save_svm_info(self):
        """@save_svm_info

        This method saves the number of features that can be expected in a
        given observation with respect to 'id_entity'.

        @self.dataset[0], we assume that validation has occurred, and safe to
            assume the data associated with the first dataset instance is
            identical to any instance n within the overall collection of
            dataset(s).

        @self.dataset['count_features'], is defined within the
            'dataset_to_dict' method.

        Note: this method needs to execute after 'dataset_to_dict'

        """

        svm_data = self.dataset[0]
        db_save = Save_Feature({
            'id_entity': svm_data['id_entity'],
            'count_features': svm_data['count_features']
        })

        # save dataset element, append error(s)
        db_return = db_save.save_count()
        if db_return['error']:
            self.list_error.append(db_return['error'])

    def validate_file_extension(self):
        """@validate_file_extension

        This method validates the file extension for each uploaded dataset,
        and returns the unique (non-duplicate) dataset.

        """

        # web-interface: validate, and restructure dataset
        if self.svm_data['data']['dataset']['file_upload']:
            validator = Validate_File_Extension(
                self.svm_data,
                self.svm_session
            )
            self.upload = validator.validate()

            if self.upload['error']:
                self.list_error.append(
                    self.upload['error']
                )
                self.flag_upload = True

        # programmatic-interface: validate, do not restructure
        elif self.svm_data['data']['dataset']['json_string']:
            self.upload = self.svm_data['data']

            if self.svm_data['error']:
                self.list_error.append(self.svm_data['error'])
                self.flag_upload = True

    def validate_id(self, session_id):
        """@validate_id

        This method validates if the session id, is a positive integer.

        """

        error = '\'session_id\' ' + session_id + ' not a positive integer'

        try:
            if not int(session_id) > 0:
                self.list_error.append(error)
        except Exception, error:
            self.list_error.append(str(error))

    def save_svm_entity(self, session_type):
        """@save_svm_entity

        This method saves the current entity into the database, then returns
        the corresponding entity id.

        """

        svm_entity = {
            'title': self.svm_data['data']['settings'].get('svm_title', None),
            'uid': self.uid,
            'id_entity': None
        }
        db_save = Save_Entity(svm_entity, session_type)

        # save dataset element
        db_return = db_save.save()

        # return error(s)
        if not db_return['status']:
            self.list_error.append(db_return['error'])
            return {'status': False, 'id': None, 'error': self.list_error}

        # return session id
        elif db_return['status'] and session_type == 'data_new':
            return {'status': True, 'id': db_return['id'], 'error': None}

    def save_svm_dataset(self):
        """@save_svm_dataset

        This method saves each dataset element (independent variable value)
        into the sql database.

        """

        for data in self.dataset:
            for dataset in data['svm_dataset']:
                db_save = Save_Feature({
                    'svm_dataset': dataset,
                    'id_entity': data['id_entity']
                })

                # save dataset element, append error(s)
                db_return = db_save.save_feature()
                if db_return['error']:
                    self.list_error.append(db_return['error'])

    def save_observation_label(self, session_type, session_id):
        """save_observation_label

        This method saves the list of unique independent variable labels,
        which can be expected in any given observation, into the sql
        database. This list of labels, is predicated on a supplied session
        id (entity id).

        @self.observation_labels, list of features (independent variables),
            defined after invoking the 'dataset_to_dict' method.

        @session_id, the corresponding returned session id from invoking the
            'save_svm_entity' method.
        """

        if len(self.observation_labels) > 0:
            for label_list in self.observation_labels:
                for label in label_list:
                    db_save = Save_Observation(
                        {
                            'label': label,
                            'id_entity': session_id
                        },
                        session_type
                    )

                    # save dataset element, append error(s)
                    db_return = db_save.save_label()
                    if not db_return['status']:
                        self.list_error.append(db_return['error'])

    def dataset_to_dict(self, id_entity):
        """@dataset_to_dict

        This method converts the supplied csv, or xml file upload(s) to a
            uniform dict object.

        @flag_append, when false, indicates the neccessary 'self.dataset' was
            not properly defined, causing this method to 'return', which
            essentially stops the execution of the current session.

        @index_count, used to 'check label consistent'.

        """

        flag_append = True
        index_count = 0
        self.dataset = []
        error_olabels = 'The supplied observation labels (dependent '\
            'variables), are inconsistent')

        try:
            # web-interface: define flag to convert to dataset to json
            if self.upload['dataset']['file_upload']:
                for val in self.upload['dataset']['file_upload']:
                    # reset file-pointer
                    val['file'].seek(0)

                    # csv to dict
                    if val['type'] == 'csv':
                        try:
                            # conversion
                            converter = Convert_Upload(val['file'])
                            converted = converter.csv_to_dict()
                            count_features = converter.get_feature_count()
                            labels = converter.get_observation_labels()

                            # check label consistency, assign labels
                            if (index_count > 0 and
                                    sorted(labels) !=
                                    sorted(self.observation_labels)):
                                self.list_error.append(error_olabels)

                            self.observation_labels.append(labels)

                            # build new (relevant) dataset
                            self.dataset.append({
                                'id_entity': id_entity,
                                'svm_dataset': converted,
                                'count_features': count_features
                            })
                        except Exception as error:
                            self.list_error.append(error)
                            flag_append = False

                    # json to dict
                    elif val['type'] == 'json':
                        try:
                            # conversion
                            converter = Convert_Upload(val['file'])
                            converted = converter.json_to_dict()
                            count_features = converter.get_feature_count()
                            labels = converter.get_observation_labels()

                            # check label consistency, assign labels
                            if (index_count > 0 and
                                    sorted(labels) !=
                                    sorted(self.observation_labels)):
                                self.list_error.append(error_olabels)

                            self.observation_labels.append(labels)

                        # build new (relevant) dataset
                            self.dataset.append({
                                'id_entity': id_entity,
                                'svm_dataset': converted,
                                'count_features': count_features
                            })
                        except Exception as error:
                            self.list_error.append(error)
                            flag_append = False

                    # xml to dict
                    elif val['type'] == 'xml':
                        try:
                            # conversion
                            converter = Convert_Upload(val['file'])
                            converted = converter.xml_to_dict()
                            count_features = converter.get_feature_count()
                            labels = converter.get_observation_labels()

                            # check label consistency, assign labels
                            if (index_count > 0 and
                                    sorted(labels) !=
                                    sorted(self.observation_labels)):
                                self.list_error.append(error_olabels)

                            self.observation_labels.append(labels)

                            # build new (relevant) dataset
                            self.dataset.append({
                                'id_entity': id_entity,
                                'svm_dataset': converted,
                                'count_features': count_features
                            })
                        except Exception as error:
                            self.list_error.append(error)
                            flag_append = False

                index_count += 1
                if not flag_append:
                    return False

            # programmatic-interface
            elif self.upload['dataset']['json_string']:
                # conversion
                dataset_json = self.upload['dataset']['json_string']
                converter = Convert_Upload(dataset_json, True)
                converted = converter.json_to_dict()
                count_features = converter.get_feature_count()
                features = dataset_json.values()[0]

                # some observations have multiple instances grouped together
                if isinstance(features, list):
                    self.observation_labels.extend(list(features[0]))
                else:
                    self.observation_labels.extend(list(features))

                for feature in dataset_json.values():
                    if isinstance(feature, list):
                        for nested_feature in feature:
                            if (sorted(self.observation_labels) !=
                                    sorted(nested_feature)):
                                self.list_error.append(error_olabels)
                    else:
                        if sorted(self.observation_labels) != sorted(feature):
                            self.list_error.append(error_olabels)

                # build dataset
                self.dataset.append({
                    'id_entity': id_entity,
                    'svm_dataset': converted,
                    'count_features': count_features
                })

        except Exception as error:
            self.list_error.append(error)
            print error
            return False

    def get_errors(self):
        """get_errors

        This method gets all current errors. associated with this class
        instance.

        """

        if len(self.list_error) > 0:
            return self.list_error
        else:
            return None
