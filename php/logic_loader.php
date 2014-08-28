<?php

/**
 * logic_loader.php
 */

/**
 * instantiate 'form_data' class
 */
 $obj = new form_data($_POST);
 logic_loader($obj);

/**
 * form_data: creates an object where properties are POST data
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
 * logic_loader(): receives the form object and determines where to allocate
 *                 parameters to respective python scripts.
 */
 function logic_loader($form) {
   if ($form == 'training') {
     print 'Welcome to training';
   }
   elseif ($form == 'analysis') {
     print 'Welcome to analysis';
   }
   else {
     print 'Error: ' . basename(__FILE__) . ', logic_loader()';
   }
 }

?>
