<?php

 /**
  * logic_loader.php: directs form POST data to respective python scripts.
  *
  *   Note: either the 'print', or 'echo' statments are used to return values back
  *         to ajax scripts.  For example, to send data to an ajax script we may
  *         have the following lines in our php script:
  *
  *           print json_encode(array('key' => 'msg')); 
  *
  *         The data can be accessed from the ajax script as follows:
  *
  *           console.log( data.key ); 
  *
  *   @json_encode( value ), returns the JSON representation of 'value'. 
  */

 /**
  * instantiate 'form_data' class
  */

 $obj = new form_data($_POST);
 logic_loader($obj);
 /**
  * form_data: 'form_data' object with properties being POST data
  *
  * @post: the post array
  */

 class form_data {
   public function __construct($post) {
     foreach($post as $key => $value) {
       $this->$key = $value;
     }
   }
 }

 /**
  * logic_loader(): receive the 'form_data' object and determines the allocation 
  *                 of its properties as parameters to respective python scripts.
  */

 function logic_loader($form) {
   if ($form->session_type == 'training') {
     print json_encode(array('msg_welcome' => print_r($_POST,true)));
     python_code('../python/svm_training.py', json_encode($form));
   }
   elseif ($form->session_type == 'analysis') {
     print json_encode(array('msg_welcome' => print_r($_POST,true)));
     python_code('../python/svm_analysis.py', json_encode($form));
   }
   else {
     print 'Error: ' . basename(__FILE__) . ', logic_loader()';
   }
 }

 /**
  * python_code(): executes python scripts using the passed in command with
  *                an optional object parameter.
  */

 function python_code($cmd, $params = '') {
   $command = escapeshellcmd($cmd);
   $parameters = escapeshellarg($params);
   $output = shell_exec("$command" . $parameters);
 }

?>
