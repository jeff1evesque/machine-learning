#!/usr/bin/python

## @svm_analysis.py
#  This file properly escapes POST data received from 'php/logic_loader.php',
#      parses the data, and sends respective portions of the POST data to
#      'python/svm_model.py'. svm_model.py is responsible for loading the
#      correct SVM model from the mySQL database, which will be used to make
#      necessary calculations / estimations.
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
  validator.data_validation()

else:
  msg = 'Please provide a training dataset in json format'
  print json.dumps({'error':msg}, separators=(',', ': '))
  sys.exit()
