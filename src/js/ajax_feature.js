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
        ajaxLoader( $('form') );
      }
    }).done(function(data) {

    // Remove AJAX Overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });

    // Append to DOM
      if (data.error) {
        $('.fieldset_session_predict').append('<div class="error">' + data.error + '</div>');
      }
      else {
          var obj_form = '\
              <fieldset class="fieldset_prediction_input">\
              <legend>Prediction Input</legend>\
            ';

            $.each($.parseJSON(data), function(index, value) {
                obj_form += '<input type="text" name="prediction_input[]" placeholder="' + value + '">';
            });

          obj_form += '</fieldset>';
      }

    // Remove previous input, add new instance
      $('.fieldset_prediction_input').remove();
      $('.fieldset_session_predict').append(obj_form);

    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);

    // Remove AJAX Overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    });
  }
