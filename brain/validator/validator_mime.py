#!/usr/bin/python

## @validator_mime.py
#  This script performs validation on the 'mime' type for file upload(s), and returns the
#      validated temporary file references(s), along with the corresponding mimetype for
#      each file upload(s).
import json, sys, magic
from brain.converter.converter_md5 import md5_for_file

## Class: Validate_Mime, explicitly inherit 'new-style' class
class Validate_Mime(object):

  ## constructor: saves a subset of the passed-in form data
  def __init__(self, svm_data, svm_session=None):
    self.svm_data    = svm_data
    self.svm_session = svm_session

  ## file_upload_validation: this method validates the MIME type of 'file upload(s)',
  #                          provided during a 'training' session. If any of the 'file
  #                          upload(s)' fails validation, this method will return False.
  #                          Otherwise, the method will return a list of unique 'file
  #                          upload(s)', discarding duplicates.
  def file_upload_validation(self, json_file_obj):
    # local variables
    list_error       = []

    json_data        = json.loads(json_file_obj)['data']['dataset']
    acceptable_type  = ['text/plain', 'text/csv', 'text/xml', 'application/xml']

    unique_hash      = set()
    json_keep        = []

    if (json_data.get('file_upload', None)):

      for index, filedata in enumerate(json_data['file_upload']):
        try:
          filehash = md5_for_file(filedata['file_temp'][0])
          # add 'hashed' value of file reference(s) to a list
          if filehash not in unique_hash:
            unique_hash.add(filehash)
            for idx, file in enumerate(filedata['file_temp']):
              mimetype = magic.from_file( file, mime=True )

              # validate mimetype
              if ( mimetype not in acceptable_type ):
                msg =  '''Problem: Uploaded file, \'''' + filedata['file_temp'][0] + '''\', must be one of the formats:'''
                msg += '\n       ' + ', '.join(acceptable_type)
                list_error.append(msg)

              # keep non-duplicated file uploads
              else:
                data = {'file_name': filedata['file_name'][idx], 'file_temp': filedata['file_temp'][idx]}
                json_keep.append( {'type': mimetype, 'filedata': data} )

        except:
          msg = 'Problem with file upload #' + str(index) + '. Please re-upload the file.'
          list_error.append(msg)

      # replace portion of JSON with unique 'file reference(s)'
      json_data['file_upload'][:] = json_keep

    else:
      msg = 'No file(s) were uploaded'
      list_error.append(msg)

    # return error
    if len(list_error) > 0:
      return { 'status': False, 'error': list_error, 'json_data': None }
    else:
      return { 'status': True, 'error': None, 'json_data': json_data }
