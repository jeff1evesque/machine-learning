<?php

/**
 * dataset.php: directs form POST data, specifically 'svm_dataset[]' to respective
 *              python scripts.
 */

// global variables
 $json = array();

// return JSON array to AJAX
 print json_encode($json);

// return 'file upload(s)' to AJAX
 var_dump($_FILES);

?>
