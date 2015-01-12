<?php

 /**
  * connector_python.php: directs form POST data to respective python scripts.
  *
  *   Note: either the 'print', or 'echo' statments are used to return values back
  *         to ajax scripts.  For example, to send data to an ajax script we may
  *         have the following lines in this php script:
  *
  *           print json_encode(array('key' => 'msg'));
  *
  *         The data can be accessed from the ajax script as follows:
  *
  *           console.log( data.key );
  *
  *   Note: to debug, or view the entire POST data array, enter the following in
  *         this php script:
  *
  *           print json_encode(array('post_array' => print_r($_POST,true)));
  *
  *         Again, the data can be accessed from the ajax script as follows:
  *
  *           console.log( data.post_array );
  *
  *   Note: performing multiple 'print json_encode( ... )' statements yields an
  *         illegal json syntax.  Specifically, it concatenates two, or more
  *         json objects. The receiving javascript file will fail overall for
  *         the ajax request, on the account of a 'Parse' error.  The receiving
  *         javascript is only allowed to receive one json representation, which
  *         may have nested json objects (not concatenated).  Therefore, only one
  *         such 'print' statement is allowed.
  *
  *   @json_encode( value ), returns the JSON representation / object of 'value'.
  *
  *   @file_temp: is a temporary reference to the 'uploaded file'.  This reference exists
  *               only for the duration of the current script, then it is automatically
  *               removed.
  */

// helper functions
  require(dirname(__FILE__) . '/helper.php');

 /**
  * Class Obj_Loader: load proper SVM session
  */
  class Obj_Loader {

   /**
    * constructor: stores form data
    */
    public function __construct($settings, $dataset) {
      $this->settings = $settings;
      $this->dataset  = $dataset;
    }

   /**
    * logic_loader(): receive the 'form_data' object, and determines the allocation
    *                 of its properties as parameters to respective python scripts.
    *
    * @json: 'reference' to the 'json' variable
    */
    public function logic_loader(&$json) {
    // local variables
      $flag_validator   = true;
      $arr_model_type   = array('classification', 'regression');
      $arr_dataset_type = array('file_upload', 'xml_url');
      $arr_session_type = array('data_new', 'data_append', 'model_generate', 'model_use');
      $arr_upload       = array();
      $arr_error        = array();
      $arr_response     = array();

    // form validation
      if (isset($this->settings->svm_session)) {
        if (!in_array(strtolower($this->settings->svm_session), $arr_session_type)) {
            array_push($arr_error, json_encode('Error: \'svm_session\' must be a string value of \'training\', or \'analysis\''));
            $flag_validator = false;
        }
      }

    // add uploaded file properties to 'arr_upload'
      $index = 0;
      foreach ($this->dataset as $val) {
        if (mb_check_encoding(json_encode($val['name']),'UTF-8') && mb_check_encoding(json_encode($val['tmp_name']),'UTF-8')) {
          $arr_upload['file_upload'][] = array(
          'file_name' => $val['name'],
          'file_temp' => $val['tmp_name'],
        );
        $index++;
      }
      else {
        array_push($arr_error, json_encode('Error: dataset filenames need to be \'UTF-8\' type string'));
        $flag_validator = false;
        break;
      }
    }
    $arr_upload['upload_quantity'] = count($this->dataset);
    unset($index);

    // Build JSON array, and send to python script
      if ($flag_validator) {
        $arr_result = array('settings' => $this->settings, 'dataset' => $arr_upload);
        $arr_result = array_merge($arr_result, array('msg_welcome' => 'Welcome to' . $this->settings->svm_session), $arr_result);
        $arr_result = array('data' => $arr_result);

        if ( isset($this->settings->svm_session) && in_array($this->settings->svm_session, $arr_session_type) ) {
          $result = shell_command('python ../../../python/load_logic.py', json_encode($arr_result));
          array_push($arr_response, json_encode($result));
        }
        else {
          array_push($arr_error, json_encode('Error: session type must be one of the following: ' . implode(', ', $arr_session_type)));\
        }
      }
      else {
        array_push( $arr_error, json_encode( array('Error' => basename(__FILE__) . ', logic_loader()') ) );
      }

    // Return Errors, and Responses
      return array('error' => $arr_error, 'response' => $arr_response);

    }
  }

?>
