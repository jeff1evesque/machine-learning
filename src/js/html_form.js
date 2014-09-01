/**
 * html_form.js: creates additional form fieldsets based on various datalist choices. 
 */

$(document).ready(function() {

// local variables
  var obj_form = {};

// append session fieldset
  $('input[name="svm_session"]').on('input', function() {
    if( $(this).val().toLowerCase() == 'analysis' ) {
      obj_form.session = '\
          <fieldset class="fieldset_session_analysis">\
            <legend>Analysis Session</legend>\
            <fieldset class="fieldset_select_model">\
              <legend>Select Model</legend>\
              <p>Select which previously stored analysis model to implement.</p>\
              <input list="analysis_models" name="svm_analysis_models" placeholder="Analysis Model"><br>\
              <datalist id="analysis_models">\
                <select name="analysis_models" required>\
                  <option value="Classification">\
                  <option value="Regression">\
                </select>\
              </datalist>\
            </fieldset>\
          </fieldset><br>\
        ';
    }
    else {
      obj_form.session = '\
          <fieldset class="fieldset_session_training">\
            <legend>Training Session</legend>\
            <fieldset class="fieldset_dataset_type">\
              <legend>Dataset Type</legend>\
              <p>Select whether the current training session will <i>upload a file</i>, or use an <i>XML file</i> for its dataset.</p>\
              <input list="dataset_type" name="svm_dataset_type" placeholder="Dataset Type"><br>\
              <datalist id="dataset_type">\
                <select name="dataset_type" required>\
                  <option value="Upload file">\
                  <option value="XML file">\
                </select>\
              </datalist>\
            </fieldset>\
          </fieldset>\
        ';
    }
    build_form('.fieldset_session_type', obj_form.session, ['.fieldset_session_analysis', '.fieldset_session_training', '.fieldset_supply_dataset']);

  // append 'Supply Dataset' fieldset
    $('input[name="svm_dataset_type"]').on('input', function() {
      if( $(this).val().toLowerCase() == 'upload file' ) {
        obj_form.dataset = '\
            <fieldset class="fieldset_supply_dataset">\
              <legend>Supply Dataset</legend>\
              <input type="file" name="svm_dataset[]" id="svm_dataset_file">\
              <input type="button" value="Add more" class="add_element svm_dataset_file_add">\
              <input type="button" value="Remove" class="remove_element svm_dataset_file_remove"><br>\
            </fieldset>\
          ';
      }
      else {
        obj_form.dataset = '\
            <fieldset class="fieldset_supply_dataset">\
              <legend>Supply Dataset</legend>\
              <input type="url" name="svm_dataset[]" placeholder="XML Dataset URL" id="svm_dataset_xml">\
              <input type="button" value="Add more" class="add_element svm_dataset_xml_add">\
              <input type="button" value="Remove" class="remove_element svm_dataset_xml_remove"><br>\
            </fieldset>\
          ';
      }
      build_form('.fieldset_dataset_type', obj_form.dataset, ['.fieldset_supply_dataset', '.fieldset_model_parameters', '.fieldset_training_type']);

  // append 'Training Type' fieldset (XML choice)
      $('input[name="svm_dataset[]"]').on('input change', function() {
        if( typeof $(this).val().toLowerCase() !== 'undefined' ) {
          obj_form.training_type = '\
              <fieldset class="fieldset_training_type">\
                <legend>Training Type</legend>\
                <p>Select whether the current training session is <i>classification</i>, or <i>regression</i>.</p>\
                <input list="training_type" name="svm_training_type" placeholder="Training Type"><br>\
                <datalist id="training_type">\
                  <select name="training_type" required>\
                    <option value="Classification">\
                    <option value="Regression">\
                  </select>\
                </datalist>\
              </fieldset>\
            ';
          build_form('.fieldset_supply_dataset', obj_form.training_type, ['.fieldset_training_type']);
        }
      });

  // append 'Training Type' fieldset (Upload File choice)
      $('input[name="svm_dataset[]"]').on('change', function() {
          obj_form.training_type = '\
              <fieldset class="fieldset_training_type">\
                <legend>Training Type</legend>\
                <p>Select whether the current training session is <i>classification</i>, or <i>regression</i>.</p>\
                <input list="training_type" name="svm_training_type" placeholder="Training Type"><br>\
                <datalist id="training_type">\
                  <select name="training_type" required>\
                    <option value="Classification">\
                    <option value="Regression">\
                  </select>\
                </datalist>\
              </fieldset>\
            ';
          build_form('.fieldset_supply_dataset', obj_form.training_type, ['.fieldset_training_type']);
      });

   // append 'Model Parameter' fieldset
      $('input[name="svm_training_type"]').on('input', function() {
        if( $(this).val().toLowerCase() == 'classification' ) {
          obj_form.model_parameters = '\
              <fieldset class="fieldset_model_parameters">\
                <legend>Classification Parameters</legend>\
                <input type="text" name="svm_clfn_dep[]" placeholder="Dependent Variable" id="svm_clfn_dep">\
                <input type="button" value="Add more" class="add_element svm_clfn_dep_add">\
                <input type="button" value="Remove" class="remove_element svm_clfn_dep_remove"><br>\
                <hr>\
                <input type="text" name="svm_clfn_indep[]" placeholder="Independent Variable" id="svm_clfn_indep">\
                <input type="button" value="Add more" class="add_element svm_clfn_indep_add">\
                <input type="button" value="Remove" class="remove_element svm_clfn_indep_remove"><br>\
              </fieldset>\
            ';
        }
        else {
          obj_form.model_parameters = '\
              <fieldset class="fieldset_model_parameters">\
                <legend>Regression Parameters</legend>\
                <input type="text" name="svm_rgrn_dep[]" placeholder="Dependent Variable" id="svm_rgrn_dep">\
                <input type="button" value="Add more" class="add_element svm_rgrn_dep_add">\
                <input type="button" value="Remove" class="remove_element svm_rgrn_dep_remove"><br>\
                <hr>\
                <input type="text" name="svm_rgrn_indep[]" placeholder="Independent Variable" id="svm_rgrn_indep">\
                <input type="button" value="Add more" class="add_element svm_rgrn_indep_add">\
                <input type="button" value="Remove" class="remove_element svm_rgrn_indep_remove"><br>\
              </fieldset>\
            ';
        }
        build_form('.fieldset_training_type', obj_form.model_parameters, ['.fieldset_model_parameters']);

      });
    });

  // append 'Known Factors / Estimated Analysis' fieldsets
    $('input[name="svm_analysis_models"]').on('input', function() {
      obj_form.analysis = '\
          <fieldset class="fieldset_known_factors">\
            <legend>Known Factors</legend>\
            <input type="text" name="svm_analysis_indep[]" placeholder="Independent Variable" id="svm_analysis_indep">\
            <input type="button" value="Add more" class="add_element svm_analysis_indep_add">\
            <input type="button" value="Remove" class="remove_element svm_analysis_indep_remove"><br>\
          </fieldset>\
          <fieldset class="fieldset_estimated_analysis">\
            <legend>Estimated Analysis</legend>\
            <p class="svm_analysis_results">Submit form for analysis results...</p>\
          </fieldset>\
        ';
      build_form('.fieldset_select_model', obj_form.analysis, ['.fieldset_known_factors', '.fieldset_estimated_analysis']);

    });
  });

/**
 * build_form: append form html
 */

  function build_form(selector, data, arr_remove) {
  // remove duplicate html
    if (typeof arr_remove !== 'undefined') {
      $.each(arr_remove, function(key, value) {
        $(value).remove();
      });
    }

  // append html
    $(selector).after(data);
  }

});
