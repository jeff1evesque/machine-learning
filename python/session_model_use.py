#!/usr/bin/python

## @session_model_use.py
#  This file receives data (i.e. settings) required to query from the database,
#      a previously stored SVM model, generated from 'session_model_generate.py'.
#      The SVM model is then used for analysis based on the input data provided
#      during this session.
#
#  Note: This script is executed from 'logic_loader.php' using the 'exec( ... )'
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
#            $output = exec("$command $parameters");
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
