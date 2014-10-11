/**
 * html_form.js: creates additional form fieldsets based on various datalist choices. 
 */

$(document).ready(function() {

// local variables
  var obj_form = {};

// append session fieldset
  $('.fieldset_session_type').on('input', 'input[name="svm_session"]', function() {
    if ( $(this).val().toLowerCase() == 'analysis' ) {
      obj_form.session = '\
          <fieldset class="fieldset_session_analysis">\
            <legend>Analysis Session</legend>\
            <fieldset class="fieldset_select_model">\
              <legend>Select Model</legend>\
              <p>Select which previously stored analysis model to implement.</p>\
              <input list="model_type" name="svm_model_type" placeholder="Analysis Model">\
              <datalist id="model_type">\
                <select name="model_type" required>\
                  <option value="Classification">Classification</option>\
                  <option value="Regression">Regression</option>\
                </select>\
              </datalist>\
            </fieldset>\
          </fieldset><br>\
        ';
    }
    else if ( $(this).val().toLowerCase() == 'training' ) {
      obj_form.session = '\
          <fieldset class="fieldset_session_training">\
            <legend>Training Session</legend>\
            <fieldset class="fieldset_dataset_type">\
              <legend>Dataset Type</legend>\
              <p>Select whether the current training session will <i>upload a file</i>, or use an <i>XML file</i> for its dataset.</p>\
              <input list="dataset_type" name="svm_dataset_type" placeholder="Dataset Type">\
              <datalist id="dataset_type">\
                <select name="dataset_type" required>\
                  <option value="Upload file">Upload file</option>\
                  <option value="XML file">XML file</option>\
                </select>\
              </datalist>\
            </fieldset>\
          </fieldset>\
        ';
    }
    else obj_form.session = null;
    build_form('.fieldset_session_type', obj_form.session, ['.fieldset_session_analysis', '.fieldset_session_training', '.fieldset_supply_dataset', '.svm_form_submit']);

  // append 'Supply Dataset' fieldset
    $('.fieldset_dataset_type').on('input', 'input[name="svm_dataset_type"]', function() {
      if ( $(this).val().toLowerCase() == 'upload file' ) {
        obj_form.dataset = '\
            <fieldset class="fieldset_supply_dataset">\
              <legend>Supply Dataset</legend>\
              <input type="file" name="svm_dataset[]" id="svm_dataset_file">\
              <input type="button" value="Add more" class="add_element svm_dataset_file_add">\
              <input type="button" value="Remove" class="remove_element svm_dataset_file_remove">\
              <p>*Note: Uploaded file(s) must be formatted as <span class="italic">plain text</span>, or <span class="italic">csv</span> format.</p>\
            </fieldset>\
          ';
      }
      else if ( $(this).val().toLowerCase() == 'xml file'  ) {
        obj_form.dataset = '\
            <fieldset class="fieldset_supply_dataset">\
              <legend>Supply Dataset</legend>\
              <input type="url" name="svm_dataset[]" placeholder="XML Dataset URL" id="svm_dataset_xml">\
              <input type="button" value="Add more" class="add_element svm_dataset_xml_add">\
              <input type="button" value="Remove" class="remove_element svm_dataset_xml_remove">\
            </fieldset>\
          ';
      }
      else obj_form.dataset = null;
      build_form('.fieldset_dataset_type', obj_form.dataset, ['.fieldset_training_parameters', '.fieldset_training_type', '.fieldset_supply_dataset']);

  // append 'Training Type' fieldset
      $('.fieldset_supply_dataset').on('input change', 'input[name="svm_dataset[]"]', function() {
        var flag_field = field_determinant( $('input[name="svm_dataset[]"]') );

        if( flag_field ) {
          obj_form.training_type = '\
              <fieldset class="fieldset_training_type">\
                <legend>Training Type</legend>\
                <p>Select whether the current training session is <i>classification</i>, or <i>regression</i>.</p>\
                <input list="model_type" name="svm_model_type" placeholder="Training Type">\
                <datalist id="model_type">\
                  <select name="model_type" required>\
                    <option value="Classification">Classification</option>\
                    <option value="Regression">Regression</option>\
                  </select>\
                </datalist>\
              </fieldset>\
            ';
        }
        else obj_form.training_type = null;
        build_form('.fieldset_supply_dataset', obj_form.training_type, ['.fieldset_training_type', '.fieldset_training_parameters', '.svm_form_submit']);

   // append 'Training Parameters' fieldset
        $('.fieldset_training_type').on('input', 'input[name="svm_model_type"]', function() {
          if ( $.inArray( $(this).val().toLowerCase(), ['classification', 'regression']) !== -1 ) {
            obj_form.training_parameters = '\
                <fieldset class="fieldset_training_parameters">\
                  <legend>' + $(this).val()  + ' Parameters</legend>\
                  <input type="text" name="svm_dep_variable[]" placeholder="Dependent Variable" id="svm_dep_variable">\
                  <input type="button" value="Add more" class="add_element svm_dep_variable_add">\
                  <input type="button" value="Remove" class="remove_element svm_dep_variable_remove">\
                  <hr>\
                  <input type="text" name="svm_indep_variable[]" placeholder="Independent Variable" id="svm_indep_variable">\
                  <input type="button" value="Add more" class="add_element svm_indep_variable_add">\
                  <input type="button" value="Remove" class="remove_element svm_indep_variable_remove">\
                </fieldset>\
              ';
            build_form('.fieldset_training_type', obj_form.training_parameters, ['.fieldset_training_parameters']);
          }
          else {
            $(this).parent().nextAll().remove();
            $(this).parent().parent().nextAll().remove();
          }

          $('.fieldset_training_parameters').on('input', ['input[name="svm_dep_variable[]"], input[name="svm_indep_variable[]"]'], function(e) {
            var flag_field_dep = field_determinant( $('input[name="svm_dep_variable[]"]') );
            var flag_field_indep = field_determinant( $('input[name="svm_indep_variable[]"]') );

            if (flag_field_dep && flag_field_indep) {
              obj_form.submit = '<input type="submit" class="svm_form_submit">';
              build_form('.fieldset_session_training', obj_form.submit, ['.svm_form_submit']);
            }
            else $('.svm_form_submit').remove();
          });
        });
      });
    });

  // append 'Known Factors' fieldset
    $('.fieldset_select_model').on('input', 'input[name="svm_model_type"]', function() {
      if ( $.inArray( $(this).val().toLowerCase(), ['classification', 'regression']) !== -1 ) {
        obj_form.analysis = '\
            <fieldset class="fieldset_known_factors">\
              <legend>Known Factors</legend>\
              <input type="text" name="svm_indep_variable[]" placeholder="Independent Variable" id="svm_indep_variable">\
              <input type="button" value="Add more" class="add_element svm_indep_variable_add">\
              <input type="button" value="Remove" class="remove_element svm_indep_variable_remove">\
            </fieldset>\
          ';
        build_form('.fieldset_select_model', obj_form.analysis, ['.fieldset_known_factors', '.fieldset_estimated_analysis', '.svm_form_submit']);
      }
      else {
        $(this).parent().nextAll().remove();
        $(this).parent().parent().nextAll().remove();
      }

  // append 'Estimated Analysis' fieldset
      $('.fieldset_known_factors').on('input change', 'input[name="svm_indep_variable[]"]', function() {
        var flag_field = field_determinant( $('input[name="svm_indep_variable[]"]') );

        if ( $(this).val().length > 0 ) {
          obj_form.estimated_analysis = '\
              <fieldset class="fieldset_estimated_analysis">\
                <legend>Estimated Analysis</legend>\
                <p class="svm_analysis_results">Waiting for results...</p>\
              </fieldset>\
            ';
          obj_form.submit = '<input type="submit" class="svm_form_submit">';
        }
        else {
          $('.fieldset_estimated_analysis').remove();
          $('.svm_analysis_submit').remove();
        }
        if (flag_field) {
          build_form('.fieldset_known_factors', obj_form.estimated_analysis, ['.fieldset_estimated_analysis']);
          build_form('.fieldset_session_analysis', obj_form.submit, ['.svm_analysis_submit']);
        }
        else $('.svm_form_submit').remove();

      });
    });
  });

/**
 * build_form: append form html
 */

  function build_form(selector, data, arr_remove) {
  // remove successive elements
    $('form '+selector).parent().nextAll().remove();
    $('form '+selector).parent().parent().nextAll().remove();

  // remove duplicate html
    if (typeof arr_remove !== 'undefined') {
      $.each(arr_remove, function(key, value) {
        $(value).remove();
      });
    }

  // append html
    $(selector).after(data);
  }

/**
 * field_determinant: if any form array fields have a string length less than
 *                    1, return false.
 */

  function field_determinant(element) {
    var num_elements = element.length;
    
    for (var i = 0; i < num_elements; i++) {
      if(element[i].value.length < 1)
        return false;
    }

    return true;
  }

});
