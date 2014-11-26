#!/usr/bin/python

## @svm_training.py
#  This file properly escapes POST data received from 'php/logic_loader.php',
#      parses the data, and sends respective portions of the POST data to
#      'python/data_creator.py'. data_creator.py is responsible for saving
#      the SVM dataset into the mySQL database.
#
#  Note: This script is executed from 'logic_loader.php' using the 'exec( ... )'
#        method. To return data to php, use a simple 'print' statement. For
#        example the following will return the arguments passed to this script:
#
#            print sys.argv[1]
#
#        Then, in php, we can capture this data by:
#
#            $output = exec("$command $parameters");
#            $arr_result = array('result' => $output);
#            $json = array_merge($json, $arr_result);
#
#        Which will allow us to return it via ajax, as follows:
#
#            print json_encode($json);
#
#        Note: we can only call `print json_encode($json)` once. The receiving
#              receiving javascript can interpret the data as follows:
#
#            console.log( data.result );
#
#  @import sys, provides various functions, and variables that can be used to
#      manipulate different parts of the Python runtime environment (i.e. argv).
#
#  Note: the term 'dataset' is used synonymously for 'file upload(s)', and XML
#        references.
import sys, json
from data_creator import Training
from data_validator import Validator
from svm_json import JSON

if len(sys.argv) > 1:
  # convert dataset to its own JSON object
  json_dataset  = JSON( sys.argv[1] )

  # validate input data is json format
  validator = Validator( sys.argv[1], 'training' )

  # validate MIME type for each dataset
  if ( json.loads(sys.argv[1])['json_creator'] == 'load_dataset.php' ):
    if ( json.loads(sys.argv[1])['data']['result'].get('file_upload', None) ):
      json_file_upload = validator.file_upload_validation( sys.argv[1] )
      if (json_file_upload is False): sys.exit()
      else: Training(json_file_upload)
  # validate, send 'training' properties (including 'xml file(s)') to 'data_creator.py'
  elif ( json.loads(sys.argv[1])['json_creator'] == 'load_logic.php' ):
    validator.data_validation()
    Training( sys.argv[1] )
else:
  msg = 'Please provide a training dataset in json format'
  print json.dumps({'error':msg}, separators=(',', ': '))
  sys.exit()
