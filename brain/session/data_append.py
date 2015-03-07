#!/usr/bin/python

## @data_append.py
#  This file receives data (i.e. settings), including one or more dataset(s)
#      provided during the current session, and stores them into corresponding
#      database tables. The stored dataset(s) can later be retrieved from
#      'data_append.py', or 'generate_model.py'.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
from brain.session.session_data_new import Data_New
from brain.database.data_saver import Data_Save

## Class: Data_Append, inherit base methods from superclass 'Data_New'
class Data_Append(Data_New):

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
  #                   'Data_New'. This method, updates an existing entity within
  #                   the corresponding database table, 'tbl_dataset_entity'.
  #
  #  @session_id, is synonymous to 'entity_id', and provides context to update
  #      'modified_xx' columns within the 'tbl_dataset_entity' database table.
  def save_svm_entity(self, session_type, session_id):
    svm_entity = {'title': self.svm_data['data']['settings'].get('svm_title', None), 'uid': 1, 'id_entity': session_id}
    db_save    = Data_Save( svm_entity, 'save_entity', session_type )

    # save dataset element
    db_return = db_save.db_data_save()

    # return error(s)
    if not db_return['status']:
      self.response_error.append( db_return['error'] )
      return { 'status': False, 'error': self.response_error }

    # return status
    elif db_return['status'] and session_type == 'data_append':
      return { 'status': True, 'error': None }
