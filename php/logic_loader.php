<?php

 /**
  * logic_loader.php: directs form POST data to respective python scripts.
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
     print 'Welcome to training';
     python_code('../python/svm_training.py', json_encode($form));
   }
   elseif ($form->session_type == 'analysis') {
     print 'Welcome to analysis';
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
   print $output;
 }

?>
