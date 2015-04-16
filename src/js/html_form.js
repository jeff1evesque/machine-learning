/**
 * html_form.js: conditionally create form fieldsets, and form elements.
 */

$(document).ready(function() {

// Local Variables
  var obj_form = {};

// Append 'Session Type' Fieldset
  $('.fieldset_session_type').on('change', 'select[name="svm_session"]', function() {
    if ( $(this).val().toLowerCase() == 'model_generate' ) {
      obj_form.session = '\
          <fieldset class="fieldset_session_generate">\
            <legend>Generate Model</legend>\
            <fieldset class="fieldset_select_model">\
              <legend>Configurations</legend>\
              <p>Select past session, and model type</p>\
              <select name="svm_session_id">\
                <option value="" selected="selected">--Select--</option>\
              </select>\
              <select name="svm_model_type">\
                <option value="" selected="selected">--Select--</option>\
                <option value="classification">Classification</option>\
                <option value="regression">Regression</option>\
              </select>\
            </fieldset>\
          </fieldset>\
        ';
    }
    else if ( $(this).val().toLowerCase() == 'model_use' ) {
      obj_form.session = '\
          <fieldset class="fieldset_session_predict">\
            <legend>Analysis</legend>\
            <fieldset class="fieldset_dataset_type">\
              <legend>Configurations</legend>\
              <p>Select a previous model to analyze</p>\
              <select name="svm_model_id">\
                <option value="" selected="selected">--Select--</option>\
              </select>\
            </fieldset>\
          </fieldset>\
        ';
    }
    else if ( $(this).val().toLowerCase() == 'data_new' ) {
      obj_form.session = '\
          <fieldset class="fieldset_session_data_upload">\
            <legend>Data Upload</legend>\
            <fieldset class="fieldset_dataset_type">\
              <legend>Configurations</legend>\
              <p>Please save the <i>Session Name</i>, then provide dataset type</p>\
              <input type="text" name="svm_title" placeholder="Session Name">\
              <select name="svm_dataset_type">\
                <option value="" selected="selected">--Select--</option>\
                <option value="file_upload">Upload file</option>\
                <option value="dataset_url">Dataset URL</option>\
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
                <option value="dataset_url">Dataset URL</option>\
              </select>\
            </fieldset>\
          </fieldset>\
        ';
    }
    else obj_form.session = null;
    build_form('.fieldset_session_type', obj_form.session, ['.fieldset_session_predict', '.fieldset_session_generate', '.fieldset_session_data_upload', '.svm_form_submit']);

  // Session Titles: for 'svm_session_id' (defined in ajax_session.js)
    if ( $.inArray( $(this).val(), ['data_append', 'model_generate'] ) !== -1 ) {
      session_id();
    }

  // Model IDs: for 'svm_model_id' (defined in ajax_model.js)
    if ( $.inArray( $(this).val(), ['model_use'] ) !== -1 ) {
      model_id();
    }

  // Submit Button: 'model_generate' case
    $('.fieldset_session_generate').on('change', 'select[name="svm_session_id"], select[name="svm_model_type"]', function() {
      if ( $('select[name="svm_session_id"]').val() && $('select[name="svm_model_type"]').val() ) {
        obj_form.submit = '<input type="submit" class="svm_form_submit">';
        build_form('.fieldset_session_generate', obj_form.submit, ['.svm_form_submit']);
      }
      else $('.svm_form_submit').remove();
    });

  // Append 'Prediction Input' Fieldset
    $('.fieldset_session_predict').on('change', 'select[name="svm_model_id"]', function() {
      if ( $('select[name="svm_model_id"]').val() ) {
        feature_properties();

        $('.fieldset_session_predict').on('change', 'input[name="indep_variable[]"]', function() {
          var flag_field = field_determinant( $('input[name="indep_variable[]"]') );

          if( flag_field ) {
            obj_form.submit = '<input type="submit" class="svm_form_submit">';
            build_form('.fieldset_session_predict', obj_form.submit, ['.svm_form_submit']);
          }
          else $('.svm_form_submit').remove();
        });

      }
    });

  // Append 'Supply Dataset' Fieldset
    $('.fieldset_session_data_upload').on('input change', 'select[name="svm_dataset_type"], select[name="svm_session_id"], input[name="svm_title"], select[name="svm_model_type"]', function() {
    // Session: Append Data
      if ( $('select[name="svm_session_id"]').val() && $('select[name="svm_dataset_type"]').val() ) {
        if ( $('select[name="svm_session_id"]').val().length > 0 && $('select[name="svm_dataset_type"]').val().toLowerCase() == 'file_upload' ) {
          obj_form.dataset = '\
              <fieldset class="fieldset_supply_dataset">\
                <legend>Supply Dataset</legend>\
                <input type="file" name="svm_dataset[]" class="svm_dataset_file">\
                <input type="button" value="Add more" class="add_element svm_dataset_file_add">\
                <input type="button" value="Remove" class="remove_element svm_dataset_file_remove">\
                <p class="form_note">*<span class="bold">Note:</span> Uploaded file(s) must be formatted as <span class="italic">csv</span>, <span class="italic">json</span>, or <span class="italic">xml</span> format.</p>\
              </fieldset>\
            ';
        }
        else if ( $('select[name="svm_session_id"]').val() > 0 && $('select[name="svm_dataset_type"]').val().toLowerCase() == 'dataset_url' ) {
          obj_form.dataset = '\
              <fieldset class="fieldset_supply_dataset">\
                <legend>Supply Dataset</legend>\
                <input type="url" name="svm_dataset[]" placeholder="Dataset URL" class="svm_dataset_xml">\
                <input type="button" value="Add more" class="add_element svm_dataset_xml_add">\
                <input type="button" value="Remove" class="remove_element svm_dataset_xml_remove">\
              </fieldset>\
            ';
        }
      }

    // Session: New Data
      else if ( $('select[name="svm_dataset_type"]').val() && $('input[name="svm_title"]').val() ) {
        if ( $('select[name="svm_dataset_type"]').val().toLowerCase() == 'file_upload' && $('input[name="svm_title"]').val().length !== 0 ) {
          obj_form.dataset = '\
              <fieldset class="fieldset_supply_dataset">\
                <legend>Supply Dataset</legend>\
                <input type="file" name="svm_dataset[]" class="svm_dataset_file">\
                <input type="button" value="Add more" class="add_element svm_dataset_file_add">\
                <input type="button" value="Remove" class="remove_element svm_dataset_file_remove">\
                <p class="form_note">*<span class="bold">Note:</span> Uploaded file(s) must be formatted as <span class="italic">csv</span>, <span class="italic">json</span>, or <span class="italic">xml</span> format.</p>\
              </fieldset>\
            ';
        }
        else if ( $('select[name="svm_dataset_type"]').val().toLowerCase() == 'dataset_url' && $('input[name="svm_title"]').val().length !== 0 ) {
          obj_form.dataset = '\
              <fieldset class="fieldset_supply_dataset">\
                <legend>Supply Dataset</legend>\
                <input type="url" name="svm_dataset[]" placeholder="Dataset URL" class="svm_dataset_xml">\
                <input type="button" value="Add more" class="add_element svm_dataset_xml_add">\
                <input type="button" value="Remove" class="remove_element svm_dataset_xml_remove">\
              </fieldset>\
            ';
        }
      }

      else obj_form.dataset = null;

    // Submit Button
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

