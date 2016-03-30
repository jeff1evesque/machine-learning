/**
 * ajax_caller.js: this script utilizes ajax to retrieve data from 'views.py'.
 *                 Specifically, an array of feature (independent variables)
 *                 names, and the generalized count of features that can be
 *                 expected within an observation, is inserted to respective
 *                 DOM elements.
 */

// AJAX Process
  function ajaxCaller(callbackDone, callbackFail, args) {
    // tell jquery to set the contentType
    if (args.contentType === null) {
      args.contentType = 'application/x-www-form-urlencoded; charset=UTF-8';
    }

    // tell jquery to process the data
    if (args.processData === null) {
      args.processData = true;
    }

    $.ajax({
      type: 'POST',
      url: args.endpoint,
      data: args.data,
      dataType: 'json',
      contentType: args.contentType,
      processData: args.processData,
      beforeSend: function() {

        // asynchronous callback
        // callbackBeforeSend();

      }
    }).done(function(data) {

      // asynchronous callback
      callbackDone(data);

    }).fail(function(jqXHR, textStatus, errorThrown) {

      // asynchronous callback
      callbackFail(textStatus, errorThrown);

    });
  }
