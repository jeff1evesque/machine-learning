#!/usr/bin/python

## @validator_mime.py
#  This script performs validation on the 'mime' type for file upload(s), and returns the
#      validated temporary file references(s), along with the corresponding mimetype for
#      each file upload(s).
import sys
from brain.converter.converter_md5 import md5_for_object

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
  def file_upload_validation(self):
    # local variables
    list_error       = []

    dataset          = self.svm_data['data']['dataset']
    acceptable_type  = ['text/plain', 'text/csv', 'text/xml', 'application/xml']

    unique_hash      = set()
    dataset_keep     = []

    if (dataset.get('file_upload', None)):

      print dataset
      for index, filedata in enumerate(dataset['file_upload']):
        try:
          filehash = md5_for_object(filedata['file'])
          # add 'hashed' value of file reference(s) to a list
          if filehash not in unique_hash:
            unique_hash.add(filehash)
            mimetype = filedata['file'].content_type

            # validate mimetype
            if ( mimetype not in acceptable_type ):
              msg = '''Problem: Uploaded file, \'''' + filedata['file_temp'][0] + '''\', must be one of the formats:'''
              msg += '\n ' + ', '.join(acceptable_type)
              list_error.append(msg)

            # keep non-duplicated file uploads
            else:
              data = {'file_name': filedata['filename'][idx], 'file': filedata['file'][idx]}
              dataset_keep.append( {'type': mimetype, 'filedata': data} )
        except:
          msg = 'Problem with file upload #' + str(index) + '. Please re-upload the file.'
          list_error.append(msg)

      # replace portion of dataset with unique 'file reference(s)'
      dataset['file_upload'][:] = dataset_keep

    else:
      msg = 'No file(s) were uploaded'
      list_error.append(msg)

    # return error
    if len(list_error) > 0:
      return { 'error': list_error, 'dataset': None }
    else:
      return { 'error': None, 'dataset': dataset }
