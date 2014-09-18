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

 /**
  * class properties
  */

 $json = array();

 /**
  * instantiate 'obj_data' class
  */

 $obj = new obj_data($_POST);
 $obj->logic_loader($obj, $json);
 print json_encode($json);

 /**
  * obj_data: copies array elements to object properties
  *
  * @arr: the array containing the elements being copied
  * @json_flag: a value of 'true' constructs a JSON friendly object, typically
  *             a response from the server side (i.e. Python).  A value of
  *             'false' constructs a simpler JSON friendly object (i.e form
  *             POST data). 
  */

 class obj_data {
   public function __construct($arr) {
     $this->arr = $arr;
     $this->obj_creator();
   }

   public function obj_creator($json_flag = false) {
     if ($json_flag === true) {
       foreach ($this->arr as $key => $value) {
       // removes additional quotes
         $temp = json_decode($value);
       // use object key, and value, instead of parent values
         foreach ($temp as $k => $v) {
           $this->$k = $v;
         }
       }
     }
     else {
       foreach($this->arr as $key => $value) {
         $this->$key = $value;
       }
     }
   }

 /**
  * logic_loader(): receive the 'form_data' object, and determines the allocation
  *                 of its properties as parameters to respective python scripts.
  *
  * @form: contains form data defined by 'form_data' class
  * @json: 'reference' to the 'json' variable
  */

   public function logic_loader($form, &$json) {
   // detect HTML5 'datalist' support
     $session_type = ($form->datalist_support) ? $form->svm_session : $form->session_type;

     if ($session_type == 'training') {
//       $result = shell_command('python ../python/svm_training.py', json_encode($form));
//       remove_quote( $result );

//       $this->arr = $result;
//       $obj_result = $this->obj_creator(true);
//       $arr_result = array('result' => $obj_result);
//       $json = array_merge($json, array('msg_welcome' => 'Welcome to training'), $arr_result);
     }
     elseif ($session_type == 'analysis') {
       $result = shell_command('python ../python/svm_analysis.py', json_encode($form));
       $arr_result = array('result' => $result);
       $json = array_merge($json, array('msg_welcome' => 'Welcome to analysis'), $arr_result);
     }
     else {
       print 'Error: ' . basename(__FILE__) . ', logic_loader()';
     }
   }
 }

 /**
  * remove_quote(): takes an array, and removes the outer quotes the from
  *                 each array element.  This function handles both single,
  *                 and double quotes.  However, the use of both (i.e. "var')
  *                 simulataneously, is incorrect syntax, and not recognized
  *                 within this function.
  *
  * @arr: passed-in array reference
  */

 function remove_quote(&$arr) {
   foreach ($arr as $key => $value) {
     $new_value = preg_replace('/^(\'(.*)\'|"(.*)")$/', '$2$3', $arr[$key]);
     $arr[$key] = $new_value;
   }
 }

 /**
  * shell_command(): executes shell scripts defined by 'cmd' with optional
  *                  parameter(s) 'param'. This function returns the result
  *                  of the executed command.
  *
  * @exec(): executes a system command
  * @output: an array filled with every line of the output from exec()
  */

 function shell_command($cmd, $params = '') {
   $command = escapeshellcmd($cmd);
   $parameters = escapeshellarg($params);

   exec("$command $parameters", $output);
   return $output;
 }

?>
