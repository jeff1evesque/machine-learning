/**
 * ajax_data.js: this script utilizes ajax to relay the form POST data, to a defined
 *               'action' script.
 */

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

    // Local Variables
    var dataset         = $('input[name="svm_dataset[]"]');
    var pInput          = $('input[name="prediction_input[]"]');
    var flagDataset     = true;
    var flagPrediction  = true;

    // Check if data supplied
    dataset.each(function() {
      if (typeof $(this).val() === 'undefined') {
        flagDataset = false;
        return false;
      }
    });
    pInput.each(function() {
      if (typeof $(this).val() === 'undefined') {
        flagPrediction = false;
        return false;
      }
    });

    // AJAX Process
    if (flagDataset || flagPrediction) {
      $.ajax({
        url: $(this).attr('action'),
        type: 'POST',
        data: new FormData(this),
        dataType: 'json',
        contentType: false,
        processData: false,
        beforeSend: function() {

          // AJAX Overlay
          ajaxLoader($(event.currentTarget));

          // Form Validation
          $('form').validate({
            submitHandler: function(form) {
              $(form).ajaxSubmit();
            }
          });
        }
      }).done(function(data) {

        // JSON Object from Server
        if (data.result) {
          var content = '\
                <fieldset class="fieldset-prediction-result">\
                  <legend>Prediction Result</legend>\
                  <p class="result"></p>\
                </fieldset>\
              ';

          if (data.result.error) {
            $('.fieldset-prediction-result').remove();
            $('.fieldset-session-predict').append(content);
            $('.result').append(data.result.error);
          } else if (data.result.result) {
            $('.fieldset-prediction-result').remove();
            $('.fieldset-session-predict').append(content);
            $('.result').append(data.result.result);
          }
        } else {
          var content = (!$.isEmptyObject(data)) ? JSON.stringify(data, undefined, 2) : 'none';
          console.log('JSON object from Server: ' + content);
        }

        // Remove AJAX Overlay
        $('form .ajax-overlay').fadeOut(200, function() { $(this).remove(); });

      }).fail(function(jqXHR, textStatus, errorThrown) {
        console.log('Error Thrown: ' + errorThrown);
        console.log('Error Status: ' + textStatus);

        // Remove AJAX Overlay
        $('form .ajax-overlay').fadeOut(200, function() { $(this).remove(); });
      });
    }

  });
});
