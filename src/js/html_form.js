/**
 * html_form.js: conditionally create form fieldsets, and form elements.
 */

$(document).ready(function() {

  // Local Variables
  var content = {};

  // Append 'Session Type' Fieldset
  $('.fieldset-session-type').on('change', 'select[name="svmSession"]', function() {
    if ($(this).val().toLowerCase() == 'model_generate') {
      content.session =
          '<fieldset class="fieldset-session-generate">' +
            '<legend>Generate Model</legend>' +
            '<fieldset class="fieldset-select-model">' +
              '<legend>Configurations</legend>' +
              '<p>Select past session, and model type</p>' +
              '<select name="svmSessionId">' +
                '<option value="" selected="selected">--Select--</option>' +
              '</select>' +
              '<select name="svmModelType">' +
                '<option value="" selected="selected">--Select--</option>' +
                '<option value="classification">Classification</option>' +
                '<option value="regression">Regression</option>' +
              '</select>' +
            '</fieldset>' +
          '</fieldset>';
    } else if ($(this).val().toLowerCase() == 'model_predict') {
      content.session =
          '<fieldset class="fieldset-session-predict">' +
            '<legend>Analysis</legend>' +
            '<fieldset class="fieldset-dataset-type">' +
              '<legend>Configurations</legend>' +
              '<p>Select a previous model to analyze</p>' +
              '<select name="svmModelId">' +
                '<option value="" selected="selected">--Select--</option>' +
              '</select>' +
            '</fieldset>' +
         '</fieldset>';
    } else if ($(this).val().toLowerCase() == 'data_new') {
      content.session =
          '<fieldset class="fieldset-session-data-upload">' +
            '<legend>Data Upload</legend>' +
            '<fieldset class="fieldset-dataset-type">' +
              '<legend>Configurations</legend>' +
              '<p>Please save the <i>Session Name</i>, then provide dataset type</p>' +
              '<input type="text" name="svmTitle" placeholder="Session Name">' +
              '<select name="svmDatasetType">' +
                '<option value="" selected="selected">--Select--</option>' +
                '<option value="file_upload">Upload file</option>' +
                '<option value="dataset_url">Dataset URL</option>' +
              '</select>' +
            '</fieldset>' +
          '</fieldset>';
    } else if ($(this).val().toLowerCase() == 'data_append') {
      content.session =
          '<fieldset class="fieldset-session-data-upload">' +
            '<legend>Data Upload</legend>' +
            '<fieldset class="fieldset-dataset-type"' +
              '<legend>Configurations</legend>' +
              '<p>Select past session, and upload type</p>' +
              '<select name="svmSessionId">' +
                '<option value="" selected="selected">--Select--</option>' +
              '</select>' +
              '<select name="svmDatasetType">' +
                '<option value="" selected="selected">--Select--</option>' +
                '<option value="file_upload">Upload file</option>' +
                '<option value="dataset_url">Dataset URL</option>' +
              '</select>' +
            '</fieldset>' +
          '</fieldset>';
    } else {
      content.session = null;
    }
    buildForm('.fieldset-session-type', content.session, ['.fieldset-session-predict', '.fieldset-session-generate', '.fieldset-session-data-upload', '.svm-form-submit']);

    // Session Titles: for 'svm_session_id' (defined in ajax_session.js)
    if ($.inArray($(this).val(), ['data_append', 'model_generate']) !== -1) {
      sessionId();
    }

    // Model IDs: for 'svm_model_id' (defined in ajax_model.js)
    if ($.inArray($(this).val(), ['model_predict']) !== -1) {
      modelId();
    }

    // Submit Button: 'model_generate' case
    $('.fieldset-session-generate').on('change', 'select[name="svmSessionId"], select[name="svmModelType"]', function() {
      if ($('select[name="svmSessionId"]').val() && $('select[name="svmModelType"]').val()) {
        content.submit = '<input type="submit" class="svm-form-submit">';
        buildForm('.fieldset-session-generate', content.submit, ['.svm_form_submit']);
      } else {
        $('.svm-form-submit').remove();
      }
    });

    // Append 'Prediction Input' Fieldset (partially define in ajax_feature.js)
    $('.fieldset-session-predict').on('change', 'select[name="svmModelId"]', function() {
      if ($('select[name="svmModelId"]').val()) {
        featureProperties();

        $('.fieldset-session-predict').on('change', 'input[name="predictionInput[]"]', function() {
          var flagField = fieldDeterminant($('input[name="predictionInput[]"]'));

          if (flagField) {
            content.submit = '<input type="submit" class="svm-form-submit">';
            buildForm('.fieldset-session-predict', content.submit, ['.svm-form-submit']);
          } else {
            $('.svm-form-submit').remove();
          }
        });

      }
    });

    // Append 'Supply Dataset' Fieldset
    $('.fieldset-session-data-upload').on('input change', 'select[name="svmDatasetType"], select[name="svmSessionId"], input[name="svmTitle"], select[name="svmModelType"]', function() {
      // Session: Append Data
      if ($('select[name="svmSessionId"]').val() && $('select[name="svmDatasetType"]').val()) {
        if ($('select[name="svmSessionId"]').val().length > 0 && $('select[name="svmDatasetType"]').val().toLowerCase() == 'file_upload') {
          content.dataset =
              '<fieldset class="fieldset-supply-dataset">' +
                '<legend>Supply Dataset</legend>' +
                '<input type="file" name="svmDataset[]" class="svm-dataset-file">' +
                '<input type="button" value="Add more" class="add-element svm-dataset-file-add">' +
                '<input type="button" value="Remove" class="remove-element svm-dataset-file-remove">' +
                '<p class="form-note">*<span class="bold">Note:</span> Uploaded file(s) must be formatted as <span class="italic">csv</span>, <span class="italic">json</span>, or <span class="italic">xml</span> format.</p>' +
              '</fieldset>';
        } else if ($('select[name="svmSessionId"]').val() > 0 && $('select[name="svmDatasetType"]').val().toLowerCase() == 'dataset_url') {
          content.dataset =
              '<fieldset class="fieldset-supply-dataset">' +
                '<legend>Supply Dataset</legend>' +
                '<input type="url" name="svmDataset[]" placeholder="Dataset URL" class="svm-dataset-xml">' +
                '<input type="button" value="Add more" class="add-element svm-dataset-xml-add">' +
                '<input type="button" value="Remove" class="remove-element svm-dataset-xml-remove">' +
              '</fieldset>';
        }
      }

      // Session: New Data
      else if ($('select[name="svmDatasetType"]').val() && $('input[name="svmTitle"]').val()) {
        if ($('select[name="svmDatasetType"]').val().toLowerCase() == 'file_upload' && $('input[name="svmTitle"]').val().length !== 0) {
          content.dataset =
              '<fieldset class="fieldset-supply-dataset">' +
                '<legend>Supply Dataset</legend>' +
                '<input type="file" name="svmDataset[]" class="svm-dataset-file">' +
                '<input type="button" value="Add more" class="add-element svm-dataset-file-add">' +
                '<input type="button" value="Remove" class="remove-element svm-dataset-file-remove">' +
                '<p class="form-note">*<span class="bold">Note:</span> Uploaded file(s) must be formatted as <span class="italic">csv</span>, <span class="italic">json</span>, or <span class="italic">xml</span> format.</p>' +
              '</fieldset>';
        } else if ($('select[name="svmDatasetType"]').val().toLowerCase() == 'dataset_url' && $('input[name="svmTitle"]').val().length !== 0) {
          content.dataset =
              '<fieldset class="fieldset-supply-dataset">' +
                '<legend>Supply Dataset</legend>' +
                '<input type="url" name="svmDataset[]" placeholder="Dataset URL" class="svm-dataset-xml">' +
                '<input type="button" value="Add more" class="add-element svm-dataset-xml-add">' +
                '<input type="button" value="Remove" class="remove-element svm-dataset-xml-remove">' +
              '</fieldset>';
        }
      } else {
        content.dataset = null;
      }

      // Submit Button
      buildForm('.fieldset-dataset-type', content.dataset, ['.fieldset-training-parameters', '.fieldset-training-type', '.fieldset-supply-dataset']);
      $('.fieldset-supply-dataset').on('change', 'input[name="svmDataset[]"]', function() {
        var flagField = fieldDeterminant($('input[name="svmDataset[]"]'));

        if (flagField) {
          content.submit = '<input type="submit" class="svm-form-submit">';
          buildForm('.fieldset-session-data-upload', content.submit, ['.svm-form-submit']);
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

