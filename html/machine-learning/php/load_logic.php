<?php

/**
 * logic_loader.php: load logic required to pass data between python scripts.
 */

// helper functions
  require(dirname(__FILE__) . '/connector_python.php');

// global variables
  $json       = array();

// debug: return 'file upload(s)' to AJAX
//  print json_encode($_FILES);

// instantiate data / loader
//  $obj_data   = new Obj_Data($_POST);
//  $obj_loader = new Obj_Loader($obj_data, $_FILES);
//  $messages   = $obj_loader->logic_loader($json);

// Return feedback to AJAX
  if ( sizeof($messages['error']) > 0 ) print json_encode( $messages['error'] );
  elseif ( sizeof($messages['response']) > 0 ) print json_encode( $messages['response'] );

?>
