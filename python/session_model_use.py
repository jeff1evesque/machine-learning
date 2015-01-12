#!/usr/bin/python

## @session_model_use.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored SVM model, generated from 'session_model_generate.py'.
#      The SVM model is then used for analysis based on the input data provided
#      during this session.
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
import sys, json
from data_creator import Analysis
from data_validator import Validator

if len(sys.argv) > 1:
  # validate input data is json format
  validator = Validator( sys.argv[1], 'analysis' )

  # validate, and set SVM properties to 'data_creator.py'
  if ( json.loads(sys.argv[1])['json_creator'] == 'load_logic.php' ):
    if ( json.loads(sys.argv[1])['data'].get('result', None) ):
      validator.data_validation()

else:
  msg = 'Please provide a training dataset in json format'
  print json.dumps({'error':msg}, separators=(',', ': '))
  sys.exit()
