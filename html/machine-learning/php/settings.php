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

  /**
   * get_db_host
   */
    public function get_db_host() {
      return $this->db_host;
    }

  /**
   * get_db_username
   */
    public function get_db_username() {
      return $this->db_username;
    }

  /**
   * get_db_password
   */
    public function get_db_password() {
      return $this->db_password;
    }

 }
