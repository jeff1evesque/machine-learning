#!/usr/bin/python

## @load_logic.py
#  This file allocates provided input to respective 'session_xxx_xxx.py' script,
#      and generates a return object as required.
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
#  Note: we can only call `print json_encode($json)` once. The receiving
#        javascript will interpret the data as follows:
#
#      console.log( data.result );
import sys, json
from session.session_data_add import Data_Add
from session.session_model_generate import Model_Generate
from session.session_model_use import Model_Use

# local variables
list_error = []

if len(sys.argv) > 1:
  # determine if input is json decodable
  try:
    session_type = json.loads(sys.argv[1])['data']['settings']['svm_session']
  except Exception as e:
    error = 'Error: the provided \'svm_session\' is not json decodable, or not defined.'
    list_error.append(error)

  # redirect input to respective 'session_xxx_xxx.py' scripts
  if session_type == 'data_new':

    # instantiate class
    session = Data_Add( sys.argv[1] )

    # implement class methods
    if not session.validate_arg_none():
      session.validate_svm_settings()
      session.validate_mime_type()
      session.check()

      session.save_svm_entity()
      session.check()

      session.dataset_to_json()
      session.validate_dataset_json()
      session.check()

      session.save_svm_dataset(session_type)
      session.check()

  elif session_type == 'data_append':

    # instantiate class
    session = Data_Add( sys.argv[1] )

    # define current session id
    session_id = json.loads(sys.argv[1])['data']['settings']['svm_session_id']

    # implement class methods
    if not session.validate_arg_none():
      session.validate_svm_settings()
      session.validate_mime_type()
      session.check()

      session.set_entity_id( session_id )

      session.dataset_to_json()
      session.validate_dataset_json()
      session.check()

      session.save_svm_dataset(session_type)
      session.check()

  elif session_type == 'model_generate':

    # instantiate class
    session = Model_Generate( sys.argv[1] )

    # implement class methods

  elif session_type == 'model_use':

    # instantiate class
    session = Model_Use( sys.argv[1] )

    # implement class methods

  else:
    error = 'Error: the provided \'svm_session\' must be \'data_new\', \'data_append\', \'model_generate\', or \'model_use\'.'
    list_error.append(error)

  # return data
  if len(list_error) > 0:
    print json.dumps({ 'status': False, 'error': list_error }, sort_keys=True, indent=2, separators=(',', ': '))
  elif len(list_error) == 0:
    print json.dumps({ 'status': True, 'error': None })
