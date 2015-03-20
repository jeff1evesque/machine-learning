#!/usr/bin/python

## @base_data.py
#  This file serves as the superclass for 'data_xx.py' files.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
from brain.database.save_entity import Save_Entity
from brain.database.save_dataset import Save_Dataset
from brain.validator.validate_dataset import Validate_Dataset
from brain.validator.validate_mime import Validate_Mime

## Class: Base_Data, explicitly inherit 'new-style' class
#
#  Note: this class is invoked within 'data_new.py'
class Base_Data(object):

    ## constructor: define class properties using the superclass 'Base'
    #               constructor, along with the constructor in this subclass.
    #
    #  @super(), implement 'Session_Base' superclass constructor within this
    #      child class constructor.
    #
    #  Note: the superclass constructor expects the same 'svm_data' argument.
    def __init__(self, svm_data):
        super(Base_Data, self).__init__(svm_data)
        self.flag_validate_mime  = False

    ## validate_mime_type: validate mime type for each dataset.
    def validate_mime_type(self):
        validator = Validate_Mime(self.svm_data, self.svm_session)
        self.response_mime_validation = validator.validate()

        if self.response_mime_validation['error'] != None:
            self.response_error.append(self.response_mime_validation['error'])
            self.flag_validate_mime = True

    ## save_svm_entity: save the current entity into the database, then return
    #                   the corresponding entity id.
    def save_svm_entity(self, session_type):
        svm_entity = {'title': self.svm_data['data']['settings'].get('svm_title', None), 'uid': 1, 'id_entity': None}
        db_save    = Save_Entity(svm_entity, session_type)

        # save dataset element
        db_return  = db_save.save()

        # return error(s)
        if not db_return['status']:
            self.response_error.append(db_return['error'])
            return {'status': False, 'id': None, 'error': self.response_error}

        # return session id
        elif db_return['status'] and session_type == 'data_new':
            return {'status': True, 'id': db_return['id'], 'error': None}

    ## validate_dataset: validate each dataset element.
    def validate_dataset(self):
        for list in self.dataset:
            for val in list['svm_dataset']:
                validated_dataset = Validate_Dataset(val, self.svm_session)

            if validated_dataset.validate()['error']:
                self.response_error.append(validated_dataset.validate()['error'])

    ## save_svm_dataset: save each dataset element into a database table.
    def save_svm_dataset(self, session_type):
        for data in self.dataset:
            for dataset in data['svm_dataset']:
                db_save = Save_Dataset({'svm_dataset': dataset, 'id_entity': data['id_entity']}, session_type)

                # save dataset element, append error(s)
                db_return = db_save.save()
                if db_return['error']: self.response_error.append(db_return['error'])
