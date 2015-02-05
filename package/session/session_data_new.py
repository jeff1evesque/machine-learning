#!/usr/bin/python

## @session_data_new.py
#  This file receives data (i.e. settings), including one or more dataset(s)
#      provided during the current session, and stores them into corresponding
#      database tables. The stored dataset(s) can later be retrieved from
#      'session_data_append.py', or 'session_generate_model.py'.
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
from session.session_data_append import Data_Append

## Class: Data_New, inherit base methods from superclass 'Data_Append'
class Data_New(Data_Append):

  ## constructor: define class properties using the superclass 'Data_Append'
  #               constructor, along with the constructor in this subclass.
  #
  #  @super(), implement 'Data_Append' superclass constructor within this
  #      child class constructor.
  #
  #  Note: the superclass constructor expects the same 'svm_data' argument.
  def __init__(self, svm_data):
    super(Data_New, self).__init__(svm_data)

  ## save_svm_entity: save entity information pertaining to new session.
  def save_svm_entity(self, session_type, session_id=None):
    svm_entity = {'title': json.loads( self.svm_data )['data']['settings'].get('svm_title', None), 'uid': 1, 'id_entity': session_id}
    db_save    = Training( svm_entity, 'save_entity', session_type )

    # save dataset element
    db_return = db_save.db_save_training()

    # return error(s)
    if not db_return['status']:
      self.response_error.append( db_return['error'] )
      return { 'id': None, 'error': self.response_error }

    # return session id
    elif db_return['status'] and session_type == 'data_new':
      return { 'id': db_return['id'], 'error': None }
