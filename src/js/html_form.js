/**
 * html_form.js: creates additional form fieldsets based on various datalist choices. 
 */

$(document).ready(function() {

// local variables
  var obj_form = {}

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
              <input type="file" name="svm_dataset_file[]" id="svm_dataset_file">\
              <input type="button" value="Add more" class="add_element svm_dataset_file_add">\
              <input type="button" value="Remove" class="remove_element svm_dataset_file_remove"><br>\
            </fieldset>\
          ';
      }
      else {
        obj_form.dataset = '\
            <fieldset class="fieldset_supply_dataset">\
              <legend>Supply Dataset</legend>\
              <input type="url" name="svm_dataset_xml[]" placeholder="XML Dataset URL" id="svm_dataset_xml">\
              <input type="button" value="Add more" class="add_element svm_dataset_xml_add">\
              <input type="button" value="Remove" class="remove_element svm_dataset_xml_remove"><br>\
            </fieldset>\
          ';
      }

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
      build_form('.fieldset_supply_datasest', obj_form.training_type);
      build_form('.fieldset_session_training', obj_form.dataset, ['.fieldset_supply_dataset']);
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
