/**
 * html_form.js: conditionally create form fieldsets, and form elements.
 */

$(document).ready(function() {

  // Local Variables
  var content = {};

  // Append 'Session Type' Fieldset
  $('.fieldset-session-type').on('change', 'select[name="svm_session"]', function() {
    if ($(this).val().toLowerCase() == 'model_generate') {
      content.session = '\
          <fieldset class="fieldset-session-generate">\
            <legend>Generate Model</legend>\
            <fieldset class="fieldset-select-model">\
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
    } else if ($(this).val().toLowerCase() == 'model_predict') {
      content.session = '\
          <fieldset class="fieldset-session-predict">\
            <legend>Analysis</legend>\
            <fieldset class="fieldset-dataset-type">\
              <legend>Configurations</legend>\
              <p>Select a previous model to analyze</p>\
              <select name="svm_model_id">\
                <option value="" selected="selected">--Select--</option>\
              </select>\
            </fieldset>\
          </fieldset>\
        ';
    } else if ($(this).val().toLowerCase() == 'data_new') {
      content.session = '\
          <fieldset class="fieldset-session-data-upload">\
            <legend>Data Upload</legend>\
            <fieldset class="fieldset-dataset-type">\
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
    } else if ($(this).val().toLowerCase() == 'data_append') {
      content.session = '\
          <fieldset class="fieldset-session-data-upload">\
            <legend>Data Upload</legend>\
            <fieldset class="fieldset-dataset-type">\
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
    } else content.session = null;
    build_form('.fieldset-session-type', content.session, ['.fieldset-session-predict', '.fieldset-session-generate', '.fieldset-session-data-upload', '.svm-form-submit']);

    // Session Titles: for 'svm_session_id' (defined in ajax_session.js)
    if ($.inArray($(this).val(), ['data_append', 'model_generate']) !== -1) {
      sessionId();
    }

    // Model IDs: for 'svm_model_id' (defined in ajax_model.js)
    if ($.inArray($(this).val(), ['model_predict']) !== -1) {
      modelId();
    }

    // Submit Button: 'model_generate' case
    $('.fieldset-session-generate').on('change', 'select[name="svm_session_id"], select[name="svm_model_type"]', function() {
      if ($('select[name="svm_session_id"]').val() && $('select[name="svm_model_type"]').val()) {
        content.submit = '<input type="submit" class="svm-form-submit">';
        build_form('.fieldset-session-generate', content.submit, ['.svm_form_submit']);
      } else $('.svm-form-submit').remove();
    });

    // Append 'Prediction Input' Fieldset (partially define in ajax_feature.js)
    $('.fieldset-session-predict').on('change', 'select[name="svm_model_id"]', function() {
      if ($('select[name="svm_model_id"]').val()) {
        featureProperties();

        $('.fieldset-session-predict').on('change', 'input[name="prediction_input[]"]', function() {
          var flag_field = field_determinant($('input[name="prediction_input[]"]'));

          if (flag_field) {
            content.submit = '<input type="submit" class="svm-form-submit">';
            build_form('.fieldset-session-predict', content.submit, ['.svm-form-submit']);
          } else $('.svm-form-submit').remove();
        });

      }
    });

    // Append 'Supply Dataset' Fieldset
    $('.fieldset_session_data_upload').on('input change', 'select[name="svm_dataset_type"], select[name="svm_session_id"], input[name="svm_title"], select[name="svm_model_type"]', function() {
      // Session: Append Data
      if ($('select[name="svm_session_id"]').val() && $('select[name="svm_dataset_type"]').val()) {
        if ($('select[name="svm_session_id"]').val().length > 0 && $('select[name="svm_dataset_type"]').val().toLowerCase() == 'file_upload') {
          content.dataset = '\
              <fieldset class="fieldset-supply-dataset">\
                <legend>Supply Dataset</legend>\
                <input type="file" name="svm_dataset[]" class="svm-dataset-file">\
                <input type="button" value="Add more" class="add-element svm-dataset-file-add">\
                <input type="button" value="Remove" class="remove-element svm-dataset-file-remove">\
                <p class="form-note">*<span class="bold">Note:</span> Uploaded file(s) must be formatted as <span class="italic">csv</span>, <span class="italic">json</span>, or <span class="italic">xml</span> format.</p>\
              </fieldset>\
            ';
        } else if ($('select[name="svm_session_id"]').val() > 0 && $('select[name="svm_dataset_type"]').val().toLowerCase() == 'dataset_url') {
          content.dataset = '\
              <fieldset class="fieldset-supply-dataset">\
                <legend>Supply Dataset</legend>\
                <input type="url" name="svm_dataset[]" placeholder="Dataset URL" class="svm-dataset-xml">\
                <input type="button" value="Add more" class="add-element svm-dataset-xml-add">\
                <input type="button" value="Remove" class="remove-element svm-dataset-xml-remove">\
              </fieldset>\
            ';
        }
      }

      // Session: New Data
      else if ($('select[name="svm_dataset_type"]').val() && $('input[name="svm_title"]').val()) {
        if ($('select[name="svm_dataset_type"]').val().toLowerCase() == 'file_upload' && $('input[name="svm_title"]').val().length !== 0) {
          content.dataset = '\
              <fieldset class="fieldset-supply-dataset">\
                <legend>Supply Dataset</legend>\
                <input type="file" name="svm_dataset[]" class="svm-dataset-file">\
                <input type="button" value="Add more" class="add-element svm-datase-file-add">\
                <input type="button" value="Remove" class="remove-element svm-dataset-file-remove">\
                <p class="form-note">*<span class="bold">Note:</span> Uploaded file(s) must be formatted as <span class="italic">csv</span>, <span class="italic">json</span>, or <span class="italic">xml</span> format.</p>\
              </fieldset>\
            ';
        } else if ($('select[name="svm_dataset_type"]').val().toLowerCase() == 'dataset_url' && $('input[name="svm_title"]').val().length !== 0) {
          content.dataset = '\
              <fieldset class="fieldset-supply-dataset">\
                <legend>Supply Dataset</legend>\
                <input type="url" name="svm_dataset[]" placeholder="Dataset URL" class="svm-dataset-xml">\
                <input type="button" value="Add more" class="add-element svm-dataset-xml-add">\
                <input type="button" value="Remove" class="remove-element svm-dataset-xml-remove">\
              </fieldset>\
            ';
        }
      } else content.dataset = null;

      // Submit Button
      build_form('.fieldset-dataset-type', content.dataset, ['.fieldset-training-parameters', '.fieldset-training-type', '.fieldset-supply-dataset']);
      $('.fieldset-supply-dataset').on('change', 'input[name="svm_dataset[]"]', function() {
        var flag_field = field_determinant($('input[name="svm_dataset[]"]'));

        if (flag_field) {
          content.submit = '<input type="submit" class="svm-form-submit">';
          build_form('.fieldset-session-data-upload', content.submit, ['.svm-form-submit']);
        } else $('.svm-form-submit').remove();
      });
    });

  });

  /**
   * build_form: append form html
   */

  function build_form(selector, data, arr_remove) {
    // remove successive elements
    $('form ' + selector).parent().nextAll().remove();
    $('form ' + selector).parent().parent().nextAll().remove();

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
      if (element[i].value.length < 1)
        return false;
    }

    return true;
  }

});

