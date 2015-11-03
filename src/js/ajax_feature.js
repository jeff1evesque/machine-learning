/**
 * ajax_feature.js: this script utilizes ajax to retrieve data from 'views.py'.
 *                  Specifically, an array of feature (independent variables)
 *                  names, and the generalized count of features that can be
 *                  expected within an observation, is inserted to respective
 *                  DOM elements.
 */

// AJAX Process
  function feature_properties() {
    var data = {'session_id': $('select[name="svm_model_id"]').val()};

    $.ajax({
      type: 'POST',
      url: '/retrieve-feature-properties/',
      data: data,
      dataType: 'json',
      beforeSend: function() {
        ajaxLoader($('form'));
      }
    }).done(function(data) {
      var content;

      // Remove AJAX Overlay
      $('form .ajax-overlay').fadeOut(200, function() { $(this).remove(); });

      // Append to DOM
      if (data.error) {
        $('.fieldset-session-predict').append('<div class="error">' + data.error + '</div>');
      } else {
        content = '\
              <fieldset class="fieldset-prediction-input">\
              <legend>Prediction Input</legend>\
            '          ;

        $.each($.parseJSON(data), function(index, value) {
          content += '<input type="text" name="prediction_input[]" placeholder="' + value + '">';
        });

        content += '</fieldset>';
      }

      // Remove previous input, add new instance
      $('.fieldset-prediction-input').remove();
      $('.fieldset-session-predict').append(content);

    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: ' + errorThrown);
      console.log('Error Status: ' + textStatus);

      // Remove AJAX Overlay
      $('form .ajax-overlay').fadeOut(200, function() { $(this).remove(); });
    });
  }
