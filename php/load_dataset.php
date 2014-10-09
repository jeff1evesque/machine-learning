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
  //var_dump($_FILES);

// local variables
  $file_name    = $_FILES['file_upload_0']['name'];
  $file_type    = $_FILES['file_upload_0']['type'];
  $file_temp    = $_FILES['file_upload_0']['tmp_name'];
  $file_size    = $_FILES['file_upload_0']['size'];

// JSON encoded 'file upload'
  $json = json_encode(array(
    'file_name'    => $file_name,
    'file_type'    => $file_type,
    'file_temp'    => $file_temp,
    'file_size'    => $file_size,
    'json_creator' => basename(__FILE__),
  ));

// send 'file upload' to python
  $result = shell_command('python ../python/svm_training.py', $json);

// return Python Data to AJAX
  print_r($result);

?>
