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
  </head>
  <body>

    <form action='../../php/logic_loader.php' method='post'>

      <fieldset>
        <legend>Session type</legend>
        <p>Select whether the current session will be <i>training</i>, or <i>analysis</i>.</p>
        <input list='session_type' name='svm_session' placeholder='Session type'><br>
        <datalist id='session_type'>
          <select name='session_type' required>
            <option value='training'>
            <option value='analysis'>
          </select>
        </datalist>
      </fieldset>

      <fieldset>
        <legend>Training Session</legend>
        <fieldset>
          <legend>Supply Dataset</legend>
          <input type='file' name='svm_dataset_file'>
          <input type='button' value='Add more' class='add_element svm_dataset_file_add'><br>
          <input type='url' name='svm_dataset_xml' placeholder='XML Dataset URL'>
          <input type='button' value='Add more' class='add_element svm_dataset_xml_add'><br>
        </fieldset>

        <fieldset>
          <legend>Classification Parameters</legend>
          <input type='text' name='svm_clfn_dep' placeholder='Dependent Variable'>
          <input type='button' value='Add more' class='add_element svm_clfn_dep_add'><br>
          <hr>
          <input type='text' name='svm_clfn_indep' placeholder='Independent Variable'>
          <input type='button' value='Add more' class='add_element svm_clfn_indep_add'><br>
        </fieldset>

        <fieldset>
          <legend>Regression Parameters</legend>
          <input type='text' name='svm_rgrn_dep' placeholder='Dependent Variable'>
          <input type='button' value='Add more' class='add_element svm_rgrn_dep_add'><br>
          <hr>
          <input type='text' name='svm_rgrn_indep' placeholder='Independent Variable'>
          <input type='button' value='Add more' class='add_element svm_rgrn_dep_add'><br>
        </fieldset>
      </fieldset><br>

      <fieldset>
        <legend>Analysis Session</legend>
        <fieldset>
          <legend>Known factors</legend>
          <input type='text' name='svm_analysis_indep' placeholder='Independent Variable'>
          <input type='button' value='Add more' class='add_element svm_analysis_indep'><br>
        </fieldset>
        <fieldset>
          <legend>Estimated Analysis</legend>
        </fieldset>
      </fieldset><br>

      <input type='submit'>

    </form>

  </body>
</html>
