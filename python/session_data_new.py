#!/usr/bin/python

## @session_data_new.py
#  This file receives data (i.e. training settings, dataset) pertaining to a
#      submitted SVM training session. The data is properly allocated to other
#      python scripts, to be validated, and properly stored into corresponding
#      EAV data model, database tables. 
#
#  Note: this script is executed from 'load_logic.php', using the 'exec( ... )'
#        equivalent method when implemented via the web-interface. Since the
#        web-interface is an AJAX process, the shelled into python script requires
#        print statements, when data is needed to be returned to the client-end.
#
#        The following will return the arguments passed into this AJAX shelled
#        into python script:
#
#            print sys.argv[1]
#
#        Then, in php, we can capture the returned data:
#
#            $output = shell_command("$command $parameters");
#            $arr_result = array('result' => $output);
#            $json = array_merge($json, $arr_result);
#
#        Which will allow us to return it to the client-end:
#
#            print json_encode($json);
#
#        Note: we can only call `print json_encode($json)` once. The receiving
#              javascript will interpret the data as follows:
#
#            console.log( data.result );
#
#  Note: the term 'dataset' used throughout various comments in this file,
#        synonymously implies the user supplied 'file upload(s)', and XML url
#        references.
import sys, json
from data_saver import Training
from data_validator import Validator
from svm_json import JSON

if len(sys.argv) > 1:
  # local variables
  response_dataset_validation = []
  flag_quit = False

  # validate SVM settings
  validator = Validator( sys.argv[1], 'training' )
  validator.data_validation()

  # validate dataset, and store dataset
  svm_entity = {'title': json.loads(sys.argv[1])['data']['settings'].get('svm_title', None), 'uid': 1}
  db_save    = Training( svm_entity, 'save_entity' )
  id_entity  = db_save.db_save_training()

  if ( json.loads(sys.argv[1])['data']['dataset'].get('file_upload', None) ):
    # validate MIME type for each dataset
    response_mime_validation = validator.file_upload_validation( sys.argv[1] )
    if ( response_mime_validation['json_data'] is False ): sys.exit()

    # convert each dataset as json, validate, and store in database
    else:
      json_dataset = {}
      svm_property = sys.argv[1]

      for val in response_mime_validation['json_data']['file_upload']:
        # csv to json
        if val['type'] in ('text/plain', 'text/csv'):
          try:
            for dataset in val['filedata']['file_temp']:
              json_dataset = {'id_entity': id_entity, 'svm_dataset': json.loads(JSON(dataset).csv_to_json())}
              json_validated = Validator( json_dataset )
              response_dataset_validation.append(json_validated.dataset_validation())

              db_save = Training( json_dataset, 'save_value' )
              db_save.db_save_training()
          except Exception as e:
            print e
            sys.exit()

        # xml to json
        elif val['type'] in ('application/xml', 'text/xml' ):
          try:
            json_dataset = {'id_entity': id_entity, 'svm_dataset': json.loads(JSON(dataset).xml_to_json())}
            json_validated = Validator( json_dataset )
            response_dataset_validation.append(json_validated.dataset_validation())

            db_save = Training( json_dataset, 'save_value' )
            db_save.db_save_training()
          except Exception as e:
            print e
            sys.exit()

  # check validation return values
  if (response_mime_validation['status'] == False):
    flag_quit = True

  for value in response_dataset_validation:
    if value['status'] == False:
      print value['error']
      flag_quit = True

  if flag_quit == True:
    sys.exit()

else:
  msg = 'Please provide a training dataset in json format'
  print json.dumps({'error':msg}, separators=(',', ': '))
  sys.exit()
