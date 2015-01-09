<?php

 /**
  * settings.php: contains various php configuration settings.
  */

 /**
  * Databas
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
   * get_db_host: get the database host
   */
    public function get_db_host() {
      return $this->db_host;
    }

  /**
   * get_db_username: get the database username
   */
    public function get_db_username() {
      return $this->db_username;
    }

  /**
   * get_db_password: get the database user password
   */
    public function get_db_password() {
      return $this->db_password;
    }

  /**
   * set_db_host: define the database host
   */
    public function set_db_host($host) {
      $this->db_host = $host;
    }

  /**
   * set_db_username: define the database user
   */
    public function set_db_username($user) {
      $this->db_username = $user;
    }

  /**
   * set_db_password: define the database password
   */
    public function set_db_password($pwd) {
      $this->db_password = $pwd;
    }

 }
