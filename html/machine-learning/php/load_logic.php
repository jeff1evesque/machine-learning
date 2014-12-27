<?php

 /**
  * logic_loader.php: directs form POST data to respective python scripts.
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
  */

// helper functions
  include(dirname(__FILE__) . '/helper.php');

// global variables
  $json = array();

// instantiate data / loader
  $obj_data   = new Obj_Data($_POST);
  $obj_loader = new Obj_Loader($obj_data);
  $obj_loader->logic_loader($json);

 /**
  * Class Obj_Loader: load proper SVM session
  */
  class Obj_Loader {

   /**
    * constructor: stores form data
    */
    public function __construct($form) {
      $this->form = $form;
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
      $arr_model_type   = Array('classification', 'regression');
      $arr_dataset_type = Array('upload file', 'xml file');
      $arr_session_type = Array('training', 'analysis');

    // HTML5 datalist supported: remove 'session_type'
      if ($this->form->datalist_support && mb_check_encoding($this->form->datalist_support, 'UTF-8')) {
        if (in_array(strtolower($this->form->svm_session), $arr_session_type)) {
          $session_type = $this->form->svm_session;
          unset($this->form->session_type);
        }
        else {
          print json_encode('Error: \'session_type\' must be string value of \'training\', or \'analysis\'');
          $flag_validator = false;
        }
      }
    // HTML5 datalist not supported: use counterpart, remove 'session_type'
      elseif (!$this->form->datalist_support && mb_check_encoding($this->form->datalist_support, 'UTF-8')) {
        if (in_array(strtolower($this->form->svm_session), $arr_session_type)) {
          $session_type            = $this->form->session_type;
          $this->form->svm_session = $session_type;
          unset($this->form->session_type);
        }
        else {
          print json_encode('Error: \'session_type\' must be string value of \'training\', or \'analysis\'');
          $flag_validator = false;
        }
      }
      else {
        print json_encode('Error: \'datalist_support\' must be a \'UTF-8\' string value');
        $flag_validator = false;
      }

      if ($session_type == 'training' && in_array(strtolower($this->form->svm_session), $arr_session_type)) {
      // Use HTML5 datalist fallback 'training_type'
        if (in_array(strtolower($this->form->model_type), $arr_model_type) && in_array(strtolower($this->form->dataset_type), $arr_dataset_type)) {
          $this->form->svm_model_type   = $this->form->model_type;
          $this->form->svm_dataset_type = $this->form->dataset_type;
          unset($this->form->model_type);
          unset($this->form->dataset_type);

        // Build JSON array, and send to python script
          if ($flag_validator) {
            $arr_result = array('result' => $this->form);
            $arr_result = array_merge($arr_result, array('msg_welcome' => 'Welcome to training'), $arr_result);
            $arr_result = array('data' => $arr_result);
            $arr_result = array_merge($arr_result, array('json_creator' => basename(__FILE__)), $arr_result);
            $result = shell_command('python ../../../python/svm_training.py', json_encode($arr_result));

          // Return JSON result(s) from python script
            print json_encode($result);
          }
        }
        else {
          print json_encode('Error: \'model_type\' must be string value of \'classification\', or \'regression\', and \'dataset_type\' must be a string value of \'upload file\', or \'xml file\'');
          $flag_validator = false;
        }
      }
      elseif ($session_type == 'analysis' && in_array(strtolower($this->form->svm_session), $arr_session_type)) {
      // Use HTML5 datalist fallback 'analysis_models'
        if (in_array(strtolower($this->form->model_type), $arr_model_type)) {
          $this->form->svm_model_type = $this->form->model_type;
          unset($this->form->model_type);

        // Build JSON array, and send to python script
          if ($flag_validator) {
            $arr_result = array('result' => $this->form);
            $arr_result = array_merge($arr_result, array('msg_welcome' => 'Welcome to analysis'), $arr_result);
            $arr_result = array('data' => $arr_result);
            $arr_result = array_merge($arr_result, array('json_creator' => basename(__FILE__)), $arr_result);
            $result     = shell_command('python ../../../python/svm_analysis.py', json_encode($arr_result));

          // Return JSON result(s) from python script
            print json_encode($result);
          }
        }
        else {
          print json_encode('Error: \'model_type\' must be string value of \'classification\', or \'regression\', and \'dataset_type\' must be a string value of \'upload file\', or \'xml file\'');
        }
      }
      else {
        print json_encode( array('Error' => basename(__FILE__) . ', logic_loader()') );
      }
    }
  }

?>
