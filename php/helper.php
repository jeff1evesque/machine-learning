<?php

 /**
  * helper.php: contains helper functions.
  */

 /**
  * Class Obj_Data: copies array elements to object properties
  *
  * @arr      : the array containing the elements being copied
  * @json_flag: a value of 'true' constructs a JSON friendly object, typically
  *             a response from the server side (i.e. Python).  A value of
  *             'false' constructs a simpler JSON friendly object (i.e form
  *             POST data).
  */

 class Obj_Data {
   public function __construct($arr, $json_flag = false) {
     if ($json_flag) {
       foreach ($arr as $key => $value) {
       // removes additional quotes
         $temp = json_decode($value);
       // use object key, and value, instead of parent values
         foreach ($temp as $k => $v) {
           $this->$k = $v;
         }
       }
     }
     else {
       foreach($arr as $key => $value) {
         $this->$key = $value;
       }
     }
   }
 }

 /**
  * remove_quote(): takes an array, and removes the outer quotes the from
  *                 each array element.  This function handles both single,
  *                 and double quotes.  However, the use of both (i.e. "var')
  *                 simulataneously, is incorrect syntax, and not recognized
  *                 within this function.
  *
  * @arr: passed-in array reference
  */

 function remove_quote(&$arr) {
   foreach ($arr as $key => $value) {
     $new_value = preg_replace('/^(\'(.*)\'|"(.*)")$/', '$2$3', $arr[$key]);
     $arr[$key] = $new_value;
   }
 }

 /**
  * shell_command(): executes shell scripts defined by 'cmd' with optional
  *                  parameter(s) 'param'. This function returns the result
  *                  of the executed command.
  *
  * @exec(): executes a system command
  * @output: an array filled with every line of the output from exec()
  */

 function shell_command($cmd, $params = '') {
   $command = escapeshellcmd($cmd);
   $parameters = escapeshellarg($params);

   exec("$command $parameters", $output);
   return $output;
 }

?>
