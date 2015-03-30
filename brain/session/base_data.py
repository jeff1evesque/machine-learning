#!/usr/bin/python

## @base_data.py
#  This file serves as the superclass for 'data_xx.py' files.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
from brain.database.save_entity import Save_Entity
from brain.database.save_feature import Save_Feature
from brain.validator.validate_mime import Validate_Mime
from brain.converter.convert_upload import Convert_Upload
from brain.database.save_observation import Save_Observation

## Class: Base_Data, explicitly inherit 'new-style' class
#
#  @self.uid, the logged-in user (i.e. userid).
#
#  Note: this class is invoked within 'data_xx.py'
class Base_Data(object):

    ## constructor:
    def __init__(self, svm_data):
        self.flag_validate_mime = False
        self.observation_labels = []
        self.list_error         = []
        self.uid                = 1

    ## save_svm_info: save the number of features that can be expected in a given
    #                 observation with respect to 'id_entity'.
    #
    #  @self.dataset[0], we assume that validation has occurred, and safe to assume
    #      the data associated with the first dataset instance is identical to any
    #      instance n within the overall collection of dataset(s).
    #
    #  @self.dataset['count_features'], is defined within the 'dataset_to_dict'
    #      method.
    #
    #  Note: this method needs to execute after 'dataset_to_dict'
    def save_svm_info(self):
        svm_data = self.dataset[0]
        db_save  = Save_Feature({'id_entity': svm_data['id_entity'], 'count_features': svm_data['count_features']})

        # save dataset element, append error(s)
        db_return = db_save.save_count()
        if db_return['error']: self.list_error.append(db_return['error'])

    ## validate_mime_type: validate mime type for each dataset.
    def validate_mime_type(self):
        validator = Validate_Mime(self.svm_data, self.svm_session)
        self.response_mime_validation = validator.validate()

        if self.response_mime_validation['error'] != None:
            self.list_error.append(self.response_mime_validation['error'])
            self.flag_validate_mime = True

    ## validate_id: validate session id as positive integer.
    def validate_id(self, session_id):
        try:
            if not int(session_id) > 0:
              self.list_error.append('supplied \'session_id\' ' + session_id + ' is not a positive integer')
        except Exception, error:
            self.list_error.append(str(error))

    ## save_svm_entity: save the current entity into the database, then return
    #                   the corresponding entity id.
    def save_svm_entity(self, session_type):
        svm_entity = {'title': self.svm_data['data']['settings'].get('svm_title', None), 'uid': self.uid, 'id_entity': None}
        db_save    = Save_Entity(svm_entity, session_type)

        # save dataset element
        db_return  = db_save.save()

        # return error(s)
        if not db_return['status']:
            self.list_error.append(db_return['error'])
            return {'status': False, 'id': None, 'error': self.list_error}

        # return session id
        elif db_return['status'] and session_type == 'data_new':
            return {'status': True, 'id': db_return['id'], 'error': None}

    ## save_svm_dataset: save each dataset element into a database table.
    def save_svm_dataset(self):
        for data in self.dataset:
            for dataset in data['svm_dataset']:
                db_save = Save_Feature({'svm_dataset': dataset, 'id_entity': data['id_entity']})

                # save dataset element, append error(s)
                db_return = db_save.save_feature()
                if db_return['error']: self.list_error.append(db_return['error'])

    ## save_observation_label: save the list of unique independent variable labels
    #                          from a supplied session (entity id) into the database.
    #
    #  @self.observation_labels, list of features (independent variables), defined
    #      after invoking the 'dataset_to_dict' method.
    #
    #  @session_id, the corresponding returned session id from invoking the
    #      'save_svm_entity' method.
    def save_observation_label(self, session_type, session_id):
        if len(self.observation_labels) > 0:
            for label in self.observation_labels:
                db_save = Save_Observation({'label': label, 'id_entity': session_id}, session_type)

                # save dataset element, append error(s)
                db_return = db_save.save_label()
                if not db_return['status']: self.list_error.append(db_return['error'])

    ## dataset_to_dict: convert either csv, or xml dataset(s) to a uniform
    #                   dict object.
    #
    #  @flag_convert, when true, indicates the file-upload mime type passed
    #      validation, and returned unique file(s) (redundancies removed).
    #
    #  @flag_append, when false, indicates the neccessary 'self.dataset' was
    #      not properly defined, causing this method to 'return', which
    #      essentially stops the execution of the current session.
    #
    #  @index_count, used to 'check label consistent'.
    def dataset_to_dict(self, id_entity):
        flag_convert = False
        flag_append  = True
        index_count  = 0

        try:
            self.response_mime_validation['dataset']['file_upload']
            flag_convert = True
        except Exception as error:
            self.list_error.append(error)
            print error
            return False

        if (flag_convert):
            self.dataset = []
            svm_property = self.svm_data

            for val in self.response_mime_validation['dataset']['file_upload']:
                # reset file-pointer
                val['file'].seek(0)

                # csv to dict
                if val['type'] in ('text/plain', 'text/csv'):
                    try:
                        # conversion
                        dataset_converter = Convert_Upload(val['file'])
                        dataset_converted = dataset_converter.csv_to_dict()
                        count_features    = dataset_converter.get_feature_count()

                        # check label consistency, assign labels
                        if index_count > 0 and sorted(dataset_converter.get_observation_labels()) != self.observation_labels: self.list_error.append('The supplied observation labels (dependent variables), are inconsistent')
                        labels = dataset_converter.get_observation_labels()
                        self.observation_labels.append(labels)

                        # build new (relevant) dataset
                        self.dataset.append({'id_entity': id_entity, 'svm_dataset': dataset_converted, 'count_features': count_features})
                    except Exception as error:
                        self.list_error.append(error)
                        flag_append = False

                # json to dict
                elif val['type'] in ('application/json'):
                    try:
                        # conversion
                        dataset_converter = Convert_Upload(val['file'])
                        dataset_converted = dataset_converter.json_to_dict()
                        count_features    = dataset_converter.get_feature_count()

                        # check label consistency, assign labels
                        if index_count > 0 and sorted(dataset_converter.get_observation_labels()) != self.observation_labels: self.list_error.append('The supplied observation labels (dependent variables), are inconsistent')
                        labels = dataset_converter.get_observation_labels()
                        self.observation_labels.append(labels)

                        # build new (relevant) dataset
                        self.dataset.append({'id_entity': id_entity, 'svm_dataset': dataset_converted, 'count_features': count_features})
                    except Exception as error:
                        self.list_error.append(error)
                        flag_append = False

                # xml to dict
                elif val['type'] in ('application/xml', 'text/xml' ):
                    try:
                        # conversion
                        dataset_converter = Convert_Upload(val['file'])
                        dataset_converted = dataset_converter.xml_to_dict()
                        count_features    = dataset_converter.get_feature_count()

                        # check label consistency, assign labels
                        if index_count > 0 and sorted(dataset_converter.get_observation_labels()) != self.observation_labels: self.list_error.append('The supplied observation labels (dependent variables), are inconsistent')
                        labels = dataset_converter.get_observation_labels()
                        self.observation_labels.append(labels)

                        # build new (relevant) dataset
                        self.dataset.append({'id_entity': id_entity, 'svm_dataset': dataset_converted, 'count_features': count_features})
                    except Exception as error:
                        self.list_error.append(error)
                        flag_append = False

            index_count += 1
            if not flag_append: return False

    # get_errors: get all current errors.
    def get_errors(self):
        if len(self.list_error) > 0:
            return self.list_error
        else:
            return None
