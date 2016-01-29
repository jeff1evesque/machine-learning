/**
 * ajax_feature.js: this script utilizes ajax to retrieve data from 'views.py'.
 *                  Specifically, an array of feature (independent variables)
 *                  names, and the generalized count of features that can be
 *                  expected within an observation, is inserted to respective
 *                  DOM elements.
 */

// AJAX Process
  function featureProperties(callbackDone, callbackFail, modelId) {
    var data = {'session_id': modelId};

    $.ajax({
      type: 'POST',
      url: '/retrieve-feature-properties/',
      data: data,
      dataType: 'json',
      beforeSend: function() {
        ajaxLoader($('form'));
      }
    }).done(function(data) {

    // asynchronous callback
      callbackDone(data);
		
    // remove ajax overlay
      $('form .ajax-overlay').fadeOut(200, function() { $(this).remove(); });

    }).fail(function(jqXHR, textStatus, errorThrown) {

    // asynchronous callback
      callbackFail(textStatus, errorThrown);

    // remove ajax overlay
      $('form .ajax-overlay').fadeOut(200, function() { $(this).remove(); });

    });
  }
