<?php

/**
 * logic_loader.php
 */

/**
 * creates an object where properties are POST data
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
 * instantiate 'form_data' class
 */
 $obj = new form_data($_POST);

?>
