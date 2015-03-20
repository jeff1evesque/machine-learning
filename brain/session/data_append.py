#!/usr/bin/python

## @data_append.py
#  This file allows methods defined from the Base, or Base_Data superclass to be
#      overridden, if needed.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
from brain.session.base import Base
from brain.session.base_data import Base_Data
from brain.database.save_entity import Save_Entity

## Class: Data_Append, inherit base methods from superclass 'Base', 'Base_Data'
#
#  Note: this class is invoked within 'load_data.py'
class Data_Append(Base, Base_Data):

    ## constructor: define class properties using the superclass 'Data_New'
    #               constructor, along with the constructor in this subclass.
    #
    #  @super(), implement 'Data_New' superclass constructor within this
    #      child class constructor.
    #
    #  Note: the superclass constructor expects the same 'svm_data' argument.
    def __init__(self, svm_data):
        super(Data_New, self).__init__(svm_data)

    ## save_svm_entity: override an identical method from inheritted superclass,
    #                   'Base_Data'. This method, updates an existing entity within
    #                   the corresponding database table, 'tbl_dataset_entity'.
    #
    #  @session_id, is synonymous to 'entity_id', and provides context to update
    #      'modified_xx' columns within the 'tbl_dataset_entity' database table.
    def save_svm_entity(self, session_type, session_id):
        svm_entity = {'title': self.svm_data['data']['settings'].get('svm_title', None), 'uid': 1, 'id_entity': session_id}
        db_save    = Save_Entity(svm_entity, session_type)

        # save dataset element
        db_return = db_save.save()

        # return error(s)
        if not db_return['status']:
            self.response_error.append(db_return['error'])
            return {'status': False, 'error': self.response_error}

        # return status
        elif db_return['status'] and session_type == 'data_append':
            return {'status': True, 'error': None}
