/**
 * ajax_feature.js: this script utilizes ajax to retrieve data from 'views.py'.
 *                  Specifically, an array of feature (independent variables)
 *                  names, and the generalized count of features that can be
 *                  expected within an observation, is inserted to respective
 *                  DOM elements.
 *
 * @args, and array of parameters (url, data).
 */

// AJAX Process
  function ajaxCaller(callbackDone, callbackFail, args) {
    $.ajax({
      type: 'POST',
      url: args['endpoint'],
      data: args['data'],
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
