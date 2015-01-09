<?php

 /**
  * settings.php
  */

 /**
  * Class Database
  */
  class Database {

  /**
   * Constructor
   */
    public function __construct() {
      $this->db_host     = 'localhost';
      $this->db_username = 'authenticated';
      $this->db_password = 'password';
    }
 }
