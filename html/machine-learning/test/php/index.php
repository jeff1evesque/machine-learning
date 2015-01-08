<!DOCTYPE html>
<?php
/**
 *  index.php: defines 'training' or 'analysis' session, prompts users to provide an upload file
 *             or URL to an XML (dataset), then defines which attributes within the dataset
 *             previously defined, to use for the SVM analysis.  After the configurations and 
 *             attributes have been defined, it is sent to 'logic_loader.py' for further analysis.
 */
?>
<html>
  <head>
    <script src='../../asset/js/jquery-2.1.1.min.js'></script>
    <script src='../../asset/js/jquery-validate.min.js'></script>
    <script src='../../asset/js/html_form.min.js'></script>
    <script src='../../asset/js/html_form_delegator.min.js'></script>
    <script src='../../asset/js/form_validator.min.js'></script>
    <script src='../../asset/js/ajax_graphic.min.js'></script>
    <script src='../../asset/js/ajax_data.min.js'></script>

    <link rel='stylesheet' href='../../asset/css/style.min.css'>
  </head>
  <body>

    <form action='../../php/load_logic.php' method='post'>
      <fieldset class='fieldset_session_type'>
        <legend>Session Type</legend>
        <p>Select data upload, or analysis session</p>
        <select name='svm_session'>
          <option value='none' selected='selected'>--Select--</option>
          <option value='data_new'>New Data</option>
          <option value='data_append'>Append Data</option>
          <option value='model_use'>Use Model</option>
        </select>
      </fieldset>
    </form>

  </body>
</html>
