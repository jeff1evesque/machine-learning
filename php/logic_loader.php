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
  *   @json_encode( value ), returns the JSON representation of 'value'. 
  */

 /**
  * instantiate 'form_data' class
  */

 $obj = new form_data($_POST);
 $json = array();

 logic_loader($obj, $json);

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

 function logic_loader($form, &$json) {
   $session_type = ($form->datalist_support) ? $form->svm_session : $form->session_type;

   if ($session_type == 'training') {
     print json_encode(array('msg_welcome' => 'Welcome to training'));
     python_code('../python/svm_training.py', json_encode($form));
   }
   elseif ($session_type == 'analysis') {
     print json_encode(array('msg_welcome' => 'Welcome to analysis'));
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
