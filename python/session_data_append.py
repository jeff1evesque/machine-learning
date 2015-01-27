#!/usr/bin/python

## @session_data_append.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored session, involving one or more stored dataset uploads,
#      and appends additional dataset(s) provided during the current session. The
#      new superset of appended dataset(s), is stored into respective database
#      table(s), which later can be retrieved in another instance of this script,
#      or within 'session_model_generate.py'.

## Class: Data_Append
class Data_Append:

  ## constructor:
  def __init__(self, svm_data):
    self.svm_data = svm_data

  ## dataset_to_json: convert either csv, or xml dataset(s) to a uniform
  #                   json object.
  def dataset_to_json(self):
    flag_convert = False
    flag_append  = True

    try:
      self.response_mime_validation['json_data']['file_upload']
      flag_convert = True
    except Exception as error:
      self.response_error.append( error )
      return False

    if ( flag_convert ):
      self.json_dataset = []
      svm_property      = self.svm_data

      for val in self.response_mime_validation['json_data']['file_upload']:
        # csv to json
        if val['type'] in ('text/plain', 'text/csv'):
          try:
            for dataset in val['filedata']['file_temp']:
              self.json_dataset.append({'id_entity': self.id_entity, 'svm_dataset': json.loads(JSON(dataset).csv_to_json())})
          except Exception as error:
            self.response_error.append( error )
            flag_append = False

        # xml to json
        elif val['type'] in ('application/xml', 'text/xml' ):
          try:
            self.json_dataset.append({'id_entity': self.id_entity, 'svm_dataset': json.loads(JSON(dataset).xml_to_json())})
          except Exception as error:
            self.response_error.append( error )
            flag_append = False

      if ( flag_append == False ): return False
