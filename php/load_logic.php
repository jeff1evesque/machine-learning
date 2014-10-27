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

// redefine JSON, and return array to AJAX
  $json['json_creator'] = basename(__FILE__);

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
    // HTML5 datalist supported: remove 'session_type'
      if ($this->form->datalist_support) {
        $session_type = $this->form->svm_session;
        unset($this->form->session_type);
      }
      else {
    // HTML5 datalist not supported: use counterpart, remove 'session_type'
        $session_type            = $this->form->session_type;
        $this->form->svm_session = $session_type;
        unset($this->form->session_type);
      }

      if ($session_type == 'training') {
      // Use HTML5 datalist fallback 'training_type'
        $this->form->svm_model_type   = $this->form->model_type;
        $this->form->svm_dataset_type = $this->form->dataset_type;
        unset($this->form->model_type);
        unset($this->form->dataset_type);

        $arr_result = array('result' => json_encode($this->form));
        $arr_result = array('data' => $arr_result);
        $result = shell_command('python ../python/svm_training.py', json_encode($arr_result));

        print json_encode($result);

      // Python returns JSON object
        if ( count((array)$result) > 0 ) {
          $json       = array_merge($json, array('msg_welcome' => 'Welcome to training'), $arr_result);
        }
      // Python returns nothing
        else {
          $json = array_merge($json, array('msg_welcome' => 'Welcome to training'));
        }
      }
      elseif ($session_type == 'analysis') {
      // Use HTML5 datalist fallback 'analysis_models'
        $this->form->svm_model_type = $this->form->model_type;
        unset($this->form->model_type);

        $arr_result = array('result' => json_encode($this->form));
        $arr_result = array('data' => $arr_result);
        $result     = shell_command('python ../python/svm_analysis.py', json_encode($arr_result));

      // Python returns JSON object
        if ( count((array)result) > 0 ) {
          $json       = array_merge($json, array('msg_welcome' => 'Welcome to analysis'), $arr_result);
        }
      // Python returns nothing
        else {
          $json = array_merge($json, array('msg_welcome' => 'Welcome to analysis'));
        }
      }
      else {
        print 'Error: ' . basename(__FILE__) . ', logic_loader()';
      }
    }
  }

?>
