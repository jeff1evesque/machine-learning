<?php

 /**
  * logic_loader.php: load associated logic required to pass data to python scripts.
  */

// helper functions
  include(dirname(__FILE__) . '/helper.php');

// global variables
  $json       = array();

// debug: return 'file upload(s)' to AJAX
//  print json_encode($_FILES);

// instantiate data / loader
  $obj_data   = new Obj_Data($_POST);
  $obj_loader = new Obj_Loader($obj_data, $_FILES);
  $messages   = $obj_loader->logic_loader($json);

// Return feedback to AJAX
  if ( sizeof($messages['error']) > 0 ) print json_encode( $messages['error'] );
  elseif ( sizeof($messages['response']) > 0 ) print json_encode( $messages['response'] );

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
      $arr_session_type = array('data_new', 'data_append', 'analysis');
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

        if ( in_array($this->settings->svm_session, array('data_new', 'data_append')) ) {
          $result = shell_command('python ../../../python/data_uploader.py', json_encode($arr_result));
        }
        else {
          $result = shell_command('python ../../../python/data_analyzer.py', json_encode($arr_result));
        }
        array_push($arr_response, json_encode($result));
      }
      else {
        array_push( $arr_error, json_encode( array('Error' => basename(__FILE__) . ', logic_loader()') ) );
      }

    // Return Errors, and Responses
      return array('error' => $arr_error, 'response' => $arr_response);

    }
  }

?>
