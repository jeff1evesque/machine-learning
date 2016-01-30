/**
 * ajax_model.js: this script utilizes ajax to retrieve data from
 *                'retriever_model.py'. Specifically, every 'svm_model' is
 *                returned.
 */

// AJAX Process
  function modelId(callbackDone, callbackFail) {
    $.ajax({
      type: 'POST',
      url: '/retrieve-model/',
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
