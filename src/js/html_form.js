/**
 * html_form.js: creates additional form fieldsets based on various datalist choices.
 */

$(document).ready(function() {

// local variables
  var obj_form = {};

// append session fieldset
  $('.fieldset_session_type').on('change', 'select[name="svm_session"]', function() {
    if ( $(this).val().toLowerCase() == 'analysis' ) {
      obj_form.session = '\
          <fieldset class="fieldset_session_analysis">\
            <legend>Analysis Session</legend>\
            <fieldset class="fieldset_select_model">\
              <legend>Select Model</legend>\
              <p>Select which previously stored analysis model to implement.</p>\
              <select name="svm_model_type">\
                <option value="" selected="selected">--Select--</option>\
                <option value="classification">Classification</option>\
                <option value="regression">Regression</option>\
              </select>\
            </fieldset>\
          </fieldset><br>\
        ';
    }
    else if ( $(this).val().toLowerCase() == 'data_new' ) {
      obj_form.session = '\
          <fieldset class="fieldset_session_data_upload">\
            <legend>Data Upload</legend>\
            <fieldset class="fieldset_dataset_type">\
              <legend>Configurations</legend>\
              <p>Please save the <i>Session Name</i>, then provide the <i>Training Type</i>, followed by the <i>Dataset Type</i></p>\
              <input type="text" name="svm_title" placeholder="Session Name">\
              <select name="svm_model_type">\
                <option value="" selected="selected">--Select--</option>\
                <option value="classification">Classification</option>\
                <option value="regression">Regression</option>\
              </select>\
              <select name="svm_dataset_type">\
                <option value="" selected="selected">--Select--</option>\
                <option value="file_upload">Upload file</option>\
                <option value="xml_url">XML URL</option>\
              </select>\
            </fieldset>\
          </fieldset>\
        ';
    }
    else if ( $(this).val().toLowerCase() == 'data_append' ) {
      obj_form.session = '\
          <fieldset class="fieldset_session_data_upload">\
            <legend>Data Upload</legend>\
            <fieldset class="fieldset_dataset_type">\
              <legend>Configurations</legend>\
              <p>Select past session, and upload type</p>\
              <select name="svm_session_id">\
                <option value="" selected="selected">--Select--</option>\
              </select>\
              <select name="svm_dataset_type">\
                <option value="" selected="selected">--Select--</option>\
                <option value="file_upload">Upload file</option>\
                <option value="xml_url">XML URL</option>\
              </select>\
            </fieldset>\
          </fieldset>\
        ';
    }
    else obj_form.session = null;
    build_form('.fieldset_session_type', obj_form.session, ['.fieldset_session_analysis', '.fieldset_session_data_upload', '.fieldset_supply_dataset', '.svm_form_submit']);

  // Add option values to 'svm_session_id' (ajax_session.js)
    if ($(this).val().toLowerCase() == 'data_append') session_id();

  // append 'Supply Dataset' fieldset (Session: Data Append)
    $('.fieldset_session_data_upload').on('input change', 'select[name="svm_dataset_type"], select[name="svm_session_id"], input[name="svm_title"], select[name="svm_model_type"]', function() {

    // append 'Supply Dataset' fieldset (Session: Append Data)
      if ( $('select[name="svm_session_id"]').val() && $('select[name="svm_dataset_type"]').val() ) {
        if ( $('select[name="svm_session_id"]').val().length > 0 && $('select[name="svm_dataset_type"]').val().toLowerCase() == 'file_upload' ) {
          obj_form.dataset = '\
              <fieldset class="fieldset_supply_dataset">\
                <legend>Supply Dataset</legend>\
                <input type="file" name="svm_dataset[]" class="svm_dataset_file">\
                <input type="button" value="Add more" class="add_element svm_dataset_file_add">\
                <input type="button" value="Remove" class="remove_element svm_dataset_file_remove">\
                <p class="form_note">*<span class="bold">Note:</span> Uploaded file(s) must be formatted as <span class="italic">csv</span>, or <span class="italic">xml</span> format.</p>\
              </fieldset>\
            ';
        }
        else if ( $('select[name="svm_session_id"]').val() > 0 && $('select[name="svm_dataset_type"]').val().toLowerCase() == 'xml_url' ) {
          obj_form.dataset = '\
              <fieldset class="fieldset_supply_dataset">\
                <legend>Supply Dataset</legend>\
                <input type="url" name="svm_dataset[]" placeholder="XML Dataset URL" class="svm_dataset_xml">\
                <input type="button" value="Add more" class="add_element svm_dataset_xml_add">\
                <input type="button" value="Remove" class="remove_element svm_dataset_xml_remove">\
              </fieldset>\
            ';
        }
      }

    // append 'Supply Dataset' fieldset (Session: New Data)
      else if ( $('select[name="svm_model_type"]').val() && $('select[name="svm_dataset_type"]').val() && $('input[name="svm_title"]').val() ) {
        if ( $.inArray( $('select[name="svm_model_type"]').val().toLowerCase(), ['classification', 'regression'] ) !== -1 && $('select[name="svm_dataset_type"]').val().toLowerCase() == 'file_upload' && $('input[name="svm_title"]').val().length !== 0 ) {
          obj_form.dataset = '\
              <fieldset class="fieldset_supply_dataset">\
                <legend>Supply Dataset</legend>\
                <input type="file" name="svm_dataset[]" class="svm_dataset_file">\
                <input type="button" value="Add more" class="add_element svm_dataset_file_add">\
                <input type="button" value="Remove" class="remove_element svm_dataset_file_remove">\
                <p class="form_note">*<span class="bold">Note:</span> Uploaded file(s) must be formatted as <span class="italic">csv</span>, or <span class="italic">xml</span> format.</p>\
              </fieldset>\
            ';
        }
        else if ( $.inArray( $('select[name="svm_model_type"]').val().toLowerCase(), ['classification', 'regression'] ) !== -1 && $('select[name="svm_dataset_type"]').val().toLowerCase() == 'xml_url' && $('input[name="svm_title"]').val().length !== 0 ) {
          obj_form.dataset = '\
              <fieldset class="fieldset_supply_dataset">\
                <legend>Supply Dataset</legend>\
                <input type="url" name="svm_dataset[]" placeholder="XML Dataset URL" class="svm_dataset_xml">\
                <input type="button" value="Add more" class="add_element svm_dataset_xml_add">\
                <input type="button" value="Remove" class="remove_element svm_dataset_xml_remove">\
              </fieldset>\
            ';
        }
      }

      else obj_form.dataset = null;

      build_form('.fieldset_dataset_type', obj_form.dataset, ['.fieldset_training_parameters', '.fieldset_training_type', '.fieldset_supply_dataset']);
      $('.fieldset_supply_dataset').on('change', 'input[name="svm_dataset[]"]', function() {
        var flag_field = field_determinant( $('input[name="svm_dataset[]"]') );

        if( flag_field ) {
          obj_form.submit = '<input type="submit" class="svm_form_submit">';
          build_form('.fieldset_session_data_upload', obj_form.submit, ['.svm_form_submit']);
        }
        else $('.svm_form_submit').remove();
      });
    });

  // append 'Known Factors' fieldset
    $('.fieldset_select_model').on('change', 'select[name="svm_model_type"]', function() {
      if ( $.inArray( $('select[name="svm_model_type"] option:selected').val().toLowerCase(), ['classification', 'regression']) !== -1 ) {
        obj_form.analysis = '\
            <fieldset class="fieldset_known_factors">\
              <legend>Known Factors</legend>\
              <input type="text" name="svm_indep_variable[]" placeholder="Independent Variable" class="svm_indep_variable">\
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

