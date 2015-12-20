/**
 * html_form.js: conditionally create form fieldsets, and form elements.
 */

$(document).ready(function() {

  // Local Variables
  var content = {};

  // Append 'Session Type' Fieldset
  $('.fieldset-session-type').on('change', 'select[name="svm_session"]', function() {
    if ($(this).val().toLowerCase() == 'model_generate') {
        require('require/model_generate');
    } else if ($(this).val().toLowerCase() == 'model_predict') {
        require('require/model_predict');
    } else if ($(this).val().toLowerCase() == 'data_new') {
        require('require/data_upload_new');
    } else if ($(this).val().toLowerCase() == 'data_append') {
        require('require/data_upload_append');
    }
    buildForm('.fieldset-session-type', null, ['.fieldset-session-predict', '.fieldset-session-generate', '.fieldset-session-data-upload', '.svm-form-submit']);

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
        buildForm('.fieldset-session-generate', null, ['.svm_form_submit']);
      } else {
        $('.svm-form-submit').remove();
      }
    });

    // Append 'Prediction Input' Fieldset (partially define in ajax_feature.js)
    $('.fieldset-session-predict').on('change', 'select[name="svm_model_id"]', function() {
      if ($('select[name="svm_model_id"]').val()) {
        featureProperties();

        $('.fieldset-session-predict').on('change', 'input[name="prediction_input[]"]', function() {
          var flagField = fieldDeterminant($('input[name="prediction_input[]"]'));

          if (flagField) {
            content.submit = '<input type="submit" class="svm-form-submit">';
            buildForm('.fieldset-session-predict', null, ['.svm-form-submit']);
          } else {
            buildForm('.fieldset-session-predict', null, ['.svm-form-submit', '.fieldset-prediction-result']);
            $('.svm-form-submit').remove();
          }
        });
      } else {
        buildForm('.fieldset-session-predict', null, ['.svm-form-submit', '.fieldset-prediction-input', '.fieldset-prediction-result']);
      }
    });

    // Append 'Supply Dataset' Fieldset
    $('.fieldset-session-data-upload').on('input change', 'select[name="svm_dataset_type"], select[name="svm_session_id"], input[name="svm_title"], select[name="svm_model_type"]', function() {
      // Session: Append Data
      if ($('select[name="svm_session_id"]').val() && $('select[name="svm_dataset_type"]').val()) {
        if ($('select[name="svm_session_id"]').val().length > 0 && $('select[name="svm_dataset_type"]').val().toLowerCase() == 'file_upload') {
          require('require/supply_dataset_file');
        } else if ($('select[name="svm_session_id"]').val() > 0 && $('select[name="svm_dataset_type"]').val().toLowerCase() == 'dataset_url') {
          content.dataset =
              require('require/supply_dataset_url');
        }
      }

      // Session: New Data
      else if ($('select[name="svm_dataset_type"]').val() && $('input[name="svm_title"]').val()) {
        if ($('select[name="svm_dataset_type"]').val().toLowerCase() == 'file_upload' && $('input[name="svm_title"]').val().length !== 0) {
          require('require/supply_dataset_file');
        } else if ($('select[name="svm_dataset_type"]').val().toLowerCase() == 'dataset_url' && $('input[name="svm_title"]').val().length !== 0) {
          require('require/supply_dataset_url');
        }
      } else {
        content.dataset = null;
      }

      // Submit Button
      buildForm('.fieldset-dataset-type', null, ['.fieldset-training-parameters', '.fieldset-training-type', '.fieldset-supply-dataset']);
      $('.fieldset-supply-dataset').on('change', 'input[name="svm_dataset[]"]', function() {
        var flagField = fieldDeterminant($('input[name="svm_dataset[]"]'));

        if (flagField) {
          content.submit = '<input type="submit" class="svm-form-submit">';
          buildForm('.fieldset-session-data-upload', null, ['.svm-form-submit']);
        } else {
          $('.svm-form-submit').remove();
        }
      });
    });

  });

  /**
   * buildForm: append form html
   */

  function buildForm(selector, data, arrRemove) {
    // remove submit button
    $('.svm-form-submit').remove();

    // remove successive elements
    $('form ' + selector).parent().nextAll().remove();
    $('form ' + selector).parent().parent().nextAll().remove();

    // remove duplicate html
    if (typeof arrRemove !== 'undefined') {
      $.each(arrRemove, function(key, value) {
        $(value).remove();
      });
    }

    // append html
    $(selector).after(data);
  }

  /**
   * fieldDeterminant: if any form array fields have a string length less than
   *                    1, return false.
   */

  function fieldDeterminant(element) {
    var numElements = element.length;

    for (var i = 0; i < numElements; i++) {
      if (element[i].value.length < 1) {
        return false;
      }
    }

    return true;
  }

});
