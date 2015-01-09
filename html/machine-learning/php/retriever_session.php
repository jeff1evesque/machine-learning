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

  if (mysqli_connect_error()) {
    $msg = array('error' => 'Connection Failed, ' . $conn->connect_error);
    print($msg);
    exit();
  }

// Query Database: output data of each row
  $sql = 'SELECT id_entity, title FROM tbl_dataset_entity';
  $result = $conn->query( $sql );

    while($row = $result->fetch_assoc()) {
      print 'id: ' . $row['id_entity']. ' title: ' . $row['title'];
    }

// Close Connection
  $conn->close();
?>
