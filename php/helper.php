<?php

 /**
  * helper.php: contains helper functions.
  */

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
