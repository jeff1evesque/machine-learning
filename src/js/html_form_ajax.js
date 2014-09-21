/**
 * html_form_ajax.js: this script prevents the form to redirect upon submission to
 *                    the 'action' page.  Instead, ajax is used to relay the forms
 *                    POST data to the 'action' script.
 *
 *                    This script implements the jquery 'event delegation' which
 *                    attaches a single event listener to a parent element, and
 *                    fires for all descendants matching a selector.
 *
 * @event.preventDefault, when this method is called, the default action of the
 *                    element will not be fired.
 *
 * @$.ajax( url [, settings] ), performs an asynchronous HTTP (Ajax) request.
 *   Required parameter -
 *     @url (required), the URL where the request is sent.
 *
 *   All settings are optional -
 *     @type, the type of request to make (default is 'GET').
 *
 *     @data, data to be sent to the server.
 *       @serializeArray(), encode a set of form elements as an array of 'names', and
 *           'values'.
 *
 *     @dataType, the type of data expected back from the server. If none is 
 *         specified, jQuery will try to infer it based on the MIME type of the
 *         response.
 *
 *     @beforeSend, a callback executed before the request is sent.
 *       @ajaxLoader(), is defined within 'ajax_loader.js'.
 *
 *   @deferred.done(function( done ) {}), replaces the deprecated jqXHR.success()
 *                    method. A function, or array of functions, that are called when
 *                    'deferred' is resolved.
 *       @data, an optional parameter representing the response data from the server
 *           side.  The server side (php) defines the data, 'msg' to return to this
 *           ajax script using the following notation:
 *
 *             print json_encode(array('key' => 'msg'));           
 *
 *           This ajax script accesses 'msg' using the following notation:
 *
 *             console.log( data.key );
 *
 *           Note: the returned data, 'data.key' can be further processed outside of
 *                 the 'console.log()' scope.
 *
 *   @defered.fail(function() {}), replaces the deprecated jqXHR.error() method. A
 *                    function, or array of functions, that are called when 'deferred'
 *                    is rejected.
 */

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

  // detect browser support for HTML5 'datalist' (IE9- / safari doesn't support it)
    var datalist_support = !!(document.createElement('datalist') && window.HTMLDataListElement);

  // serialize data into array
    var data_formatted = $('form').serializeArray();
    data_formatted.push({ name: 'datalist_support', value: datalist_support });

  // ajax request
    $.ajax({
      url: $(this).attr('action'),
      type: 'POST',
      data : data_formatted,
      dataType : 'json',
      beforeSend: function() {
  // ajax overlay
        ajaxLoader( $(event.currentTarget) );
      }
    }).done(function(data) {
  // JSON object from Server
      json_server = ( !$.isEmptyObject( data.result ) ) ? JSON.stringify(data.result) : 'none';
      console.log( data.msg_welcome );
      console.log( 'JSON object from Server: ' + json_server );

  // server side error
      $('form .fieldset_error').remove();
      if (typeof data.result.error !== 'undefined') {
        var msg_error = '\
            <fieldset class="fieldset_error">\
              <legend>Submission Error</legend>\
              <p>Error: '+data.result.error+'</p>\
            </fieldset>\
          ';
        $('form').prepend(msg_error);
      }

  // remove ajax overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    }).fail(function(jqXHR, textStatus, errorThrown) {
      $('form .fieldset_error').remove();

      var msg_error = '\
          <fieldset class="fieldset_error">\
            <legend>Submission Error</legend>\
            <p>Error: '+errorThrown+'</p>\
          </fieldset>\
        ';
     $('form').prepend(msg_error);

      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);
    });

  });
});
