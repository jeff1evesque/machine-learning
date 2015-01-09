<?php

 /**
  * retriever_session.php: query 'svm_title', and 'id_entity' value from database.
  *                        Then, return the two corresponding values via AJAX to
  *                        'ajax_session.js'
  */

  include(dirname(__FILE__) . '/settings.php');

// Local Variables
  $db_settings = new Database();
  $db_name     = 'db_machine_learning';

// Create Connection
  $conn = new mysqli( $db_settings->db_host, $db_settings->db->username, $db_settings->password, $db_name );

?>
