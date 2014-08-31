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
      </fieldset>

      <fieldset class='fieldset_training_session'>
        <legend>Training Session</legend>

        <fieldset class='fieldset_dataset_type'>
          <legend>Dataset Type</legend>
          <p>Select whether the current training session will <i>upload a file</i>, or use an <i>XML file</i> for its dataset.</p>
          <input list='dataset_type' name='svm_dataset_type' placeholder='Dataset Type'><br>
          <datalist id='dataset_type'>
            <select name='dataset_type' required>
              <option value='Upload file'>
              <option value='XML file'>
            </select>
          </datalist>
        </fieldset>

        <fieldset class='fieldset_supply_dataset'>
          <legend>Supply Dataset</legend>
          <input type='file' name='svm_dataset_file[]' id='svm_dataset_file'>
          <input type='button' value='Add more' class='add_element svm_dataset_file_add'>
          <input type='button' value='Remove' class='remove_element svm_dataset_file_remove'><br>
          <input type='url' name='svm_dataset_xml[]' placeholder='XML Dataset URL' id='svm_dataset_xml'>
          <input type='button' value='Add more' class='add_element svm_dataset_xml_add'>
          <input type='button' value='Remove' class='remove_element svm_dataset_xml_remove'><br>
        </fieldset>

        <fieldset class='fieldset_training_type'>
          <legend>Training Type</legend>
          <p>Select whether the current training session is <i>classification</i>, or <i>regression</i>.</p>
          <input list='training_type' name='svm_training_type' placeholder='Training Type'><br>
          <datalist id='training_type'>
            <select name='training_type' required>
              <option value='Classification'>
              <option value='Regression'>
            </select>
          </datalist>
        </fieldset>

        <fieldset class='fieldset_classification_parameters'>
          <legend>Classification Parameters</legend>
          <input type='text' name='svm_clfn_dep[]' placeholder='Dependent Variable' id='svm_clfn_dep'>
          <input type='button' value='Add more' class='add_element svm_clfn_dep_add'>
          <input type='button' value='Remove' class='remove_element svm_clfn_dep_remove'><br>
          <hr>
          <input type='text' name='svm_clfn_indep[]' placeholder='Independent Variable' id='svm_clfn_indep'>
          <input type='button' value='Add more' class='add_element svm_clfn_indep_add'>
          <input type='button' value='Remove' class='remove_element svm_clfn_indep_remove'><br>
        </fieldset>

        <fieldset class='fieldset_regression_parameters'>
          <legend>Regression Parameters</legend>
          <input type='text' name='svm_rgrn_dep[]' placeholder='Dependent Variable' id='svm_rgrn_dep'>
          <input type='button' value='Add more' class='add_element svm_rgrn_dep_add'>
          <input type='button' value='Remove' class='remove_element svm_rgrn_dep_remove'><br>
          <hr>
          <input type='text' name='svm_rgrn_indep[]' placeholder='Independent Variable' id='svm_rgrn_indep'>
          <input type='button' value='Add more' class='add_element svm_rgrn_indep_add'>
          <input type='button' value='Remove' class='remove_element svm_rgrn_indep_remove'><br>
        </fieldset>
      </fieldset><br>

      <fieldset class='fieldset_analysis_session'>
        <legend>Analysis Session</legend>

        <fieldset class='fieldset_select_model'>
          <legend>Select Model</legend>
          <p>Select which previously stored analysis model to implement.</p>
          <input list='analysis_models' name='svm_analysis_models' placeholder='Analysis Model'><br>
          <datalist id='analysis_models'>
            <select name='analysis_models' required>
              <option value='Classification'>
              <option value='Regression'>
            </select>
          </datalist>
        </fieldset>

        <fieldset class='fieldset_known_factors'>
          <legend>Known Factors</legend>
          <input type='text' name='svm_analysis_indep[]' placeholder='Independent Variable' id='svm_analysis_indep'>
          <input type='button' value='Add more' class='add_element svm_analysis_indep_add'>
          <input type='button' value='Remove' class='remove_element svm_analysis_indep_remove'><br>
        </fieldset>
        <fieldset class='fieldset_estimated_analysis'>
          <legend>Estimated Analysis</legend>
        </fieldset>
      </fieldset><br>

      <input type='submit'>

    </form>

  </body>
</html>
