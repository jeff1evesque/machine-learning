/**
 * ajax_session.js: this script utilizes ajax to retrieve data from
 *                  'retriever_session.py'. Specifically, the 'svm_title', and
 *                  'id_entity' values are taken from EAV data model, database
 *                  tables, and inserted into the DOM element 'svm_session_id'.
 */

// AJAX Process
  function sessionId(callbackDone, callbackFail) {
    $.ajax({
      type: 'POST',
      url: '/retrieve-session/',
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
