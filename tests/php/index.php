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
  </head>
  <body>

    <form action='../../php/logic_loader.php' method='post'>

      <fieldset>
        <legend>Session type</legend><br>
        <input list='session_type' name='svm_session'><br>
        <datalist id='session_type'>
          <select name='session_type' required>
            <option value='training'>
            <option value='analysis'>
          </select>
        </datalist>
      </fieldset>

      <fieldset>
        <legend>Data Input</legend>
        <label>Supply Dataset</label><br>
        <input type='file' name='svm_dataset_file'><br>
        <input type='url' name='svm_dataset_xml'><br>

        <label>Classification Parameters</label><br>
        <input type='text' name='svm_clfn_dep'><br>
        <input type='text' name='svm_clfn_indep'><br>

        <label>Regression Parameters</label><br>
        <input type='text' name='svm_rgrn_dep'><br>
        <input type='text' name='svm_rgrn_indep'><br>
      </fieldset><br>

      <input type='submit'>

    </form>

  </body>
</html>
