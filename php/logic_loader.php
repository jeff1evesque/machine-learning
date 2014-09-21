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
 $obj_data = new Obj_Data($_POST);
 $obj_loader = new Obj_Loader($obj_data);
 $obj_loader->logic_loader($json);

// return JSON array to AJAX
 print json_encode($json);

 /**
  * Class Obj_Data: copies array elements to object properties
  *
  * @arr      : the array containing the elements being copied
  * @json_flag: a value of 'true' constructs a JSON friendly object, typically
  *             a response from the server side (i.e. Python).  A value of
  *             'false' constructs a simpler JSON friendly object (i.e form
  *             POST data).
  */

 class Obj_Data {
   public function __construct($arr, $json_flag = false) {
     if ($json_flag) {
       foreach ($arr as $key => $value) {
       // removes additional quotes
         $temp = json_decode($value);
       // use object key, and value, instead of parent values
         foreach ($temp as $k => $v) {
           $this->$k = $v;
         }
       }
     }
     else {
       foreach($arr as $key => $value) {
         $this->$key = $value;
       }
     }
   }
 }

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
   // session type corresponding on HTML5 'datalist' support
     $session_type = ($this->form->datalist_support) ? $this->form->svm_session : $this->form->session_type;

     if ($session_type == 'training') {
       $result = shell_command('python ../python/svm_training.py', json_encode($this->form));
       remove_quote( $result );
       $obj_result = new Obj_Data($result, true);
       $arr_result = array('result' => $obj_result);
       $json = array_merge($json, array('msg_welcome' => 'Welcome to training'), $arr_result);
     }
     elseif ($session_type == 'analysis') {
       $result = shell_command('python ../python/svm_analysis.py', json_encode($this->form));
       remove_quote( $result );
       $obj_result = new Obj_Data($result, true);

     // Python returns JSON object
       if ( count((array)$obj_result) > 0 ) {
         $arr_result = array('result' => $obj_result);
         $json = array_merge($json, array('msg_welcome' => 'Welcome to analysis'), $arr_result);
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
