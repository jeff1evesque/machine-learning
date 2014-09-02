<!DOCTYPE html>
<?php
/**
 *  index.php: defines 'training' or 'analysis' session, prompts users to provide an upload file
 *             or URL to an XML (dataset), then defines which attributes within the dataset
 *             previously defined, to use for the SVM analysis.  After the configurations and 
 *             attributes have been defined, it is sent to 'logic_loader.py' for further analysis.
 *
 *  @form:     sends form-data to 'logic_loader.py' using the 'post' method.
 *
 *  @input:    uses the 'list' attribute to refer to the datalist element which contains
 *             pre-defined options for this input element.
 *
 *  @datalist: an HTML5 tag that specifies a list of pre-defined options for an input element.
 *             Since this is not supported in IE9-, or Safari, the 'select' element is nested
 *             inside the 'datalist'.  This allows for graceful degradation.
 */
?>
<html>
  <head>
    <script src='../../src/js/jquery-1.8.3.js'></script>
    <script src='../../src/js/html_form.js'></script>
    <script src='../../src/js/html_form_delegator.js'></script>

    <link rel='stylesheet' href=''../../src/css/form_svm.css'>
  </head>
  <body>

    <form action='../../php/logic_loader.php' method='post'>

      <fieldset class='fieldset_session_type'>
        <legend>Session Type</legend>
        <p>Select whether the current session will be <i>training</i>, or <i>analysis</i>.</p>
        <input list='session_type' name='svm_session' placeholder='Session Type'><br>
        <datalist id='session_type'>
          <select name='session_type' required>
            <option value='training'>
            <option value='analysis'>
          </select>
        </datalist>
      </fieldset><br>

    </form>

  </body>
</html>
