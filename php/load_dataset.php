<?php

/**
 * dataset.php: directs form POST data, specifically 'svm_dataset[]' to respective
 *              python scripts.
 *
 * @file_temp: is a temporary reference to the 'uploaded file'.  This reference exists
 *   only for the duration of the current script, then it is automatically removed.
 */

// helper functions
  include(dirname(__FILE__) . '/helper.php');

// debug: return 'file upload(s)' to AJAX
  var_dump($_FILES);
  print count($_FILES);

// local variables
  $arr_upload = Array();

// add uploaded file properties to 'arr_upload'
  $index = 0;
  foreach ($_FILES as $val) {
    $arr_upload['file_upload'][] = array(
      $_FILES['file_upload_' + index]['name'] = $_FILES['file_upload_' + index]['tmp_name'];
    );
    $index++;
  }
  $arr_upload['json_creator'] = basename(__FILE__);

// JSON encode 'arr_upload'
  $json = json_encode( $arr_upload );

// send 'file upload' to python
  $result = shell_command('python ../python/svm_training.py', $json);

// return Python Data to AJAX
  print_r($result);

?>
