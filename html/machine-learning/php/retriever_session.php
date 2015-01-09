<?php error_reporting(-1); ini_set('display_errors', 1); ?>

<?php

 /**
  * retriever_session.php: query 'svm_title', and 'id_entity' value from database.
  *                        Then, return the two corresponding values via AJAX to
  *                        'ajax_session.js'
  */

  require(dirname(__FILE__) . '/settings.php');

// Local Variables
  $db_settings = new Database();
  $db_name     = 'db_machine_learning';
  $arr_return  = array();

// Create Connection
  $conn = new mysqli( $db_settings->db_host, $db_settings->db_username, $db_settings->db_password, $db_name );

  if (mysqli_connect_error()) {
    $msg = array('error' => 'Connection Failed, ' . $conn->connect_error);
    print($msg);
    exit();
  }

// Query Database: output data of each row
  $sql = 'SELECT id_entity, title FROM tbl_dataset_entity';

  if ( $result = $conn->query($sql) ) {
    while($row = $result->fetch_row()) {
      array_push($arr_return, array('id' => $row[0], 'title' => $row[1]));
    }

    $result->close();
  }

// Close Connection
  $conn->close();
?>
