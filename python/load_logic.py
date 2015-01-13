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

if len(sys.argv) > 1:
  try:
    session_type = json.loads(sys.argv[1])['data']['settings']['svm_session']
    print session_type
  except Exception as e:
    print e
    sys.exit()
