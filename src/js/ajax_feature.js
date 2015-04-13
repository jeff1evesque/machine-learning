/**
 * ajax_feature.js: this script utilizes ajax to retrieve data from 'views.py'.
 *                  Specifically, an array of feature (independent variables)
 *                  names, and the generalized count of features that can be
 *                  expected within an observation, is inserted to respective
 *                  DOM elements.
 */

// AJAX Process
  function feature_properties() {
    var session_id = $('select[name="svm_model_id"]').val();

    $.ajax({
      type: 'POST',
      url: '/retrieve-feature-properties/',
      data: JSON.stringify({'session_id': session_id});
      dataType: 'json',
      beforeSend: function() {
        ajaxLoader( $('form') );
      }
    }).done(function(data) {

    // Remove AJAX Overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });

    // Append to DOM
      if (data.error) {
        $('.fieldset_session_analysis').append('<div class="error">' + data.error + '</div>');
      }
      else {
        return data.features;
      }

    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);

    // Remove AJAX Overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    });
  }
