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
 *     @beforeSend, a callback executed before the request is sent.
 *       @ajaxLoader(), is defined within 'ajax_loader.js'.
 *
 *   @deferred.done(function() {}), replaces the deprecated jqXHR.success() method. A
 *                    function, or array of functions, that are called when 'deferred'
 *                    is resolved.
 *
 *   @deffered.fail(function() {}), replaces the deprecated jqXHR.error() method. A
 *                    function, or array of functions, that are called when 'deferred'
 *                    is rejected.
 */

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

    $.ajax({
      url: $(this).attr('action'),
      type: 'POST',
      beforeSend: function() {
        ajaxLoader( $(event.currentTarget) );
      }
    }).done(function(data) {
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    }).fail(function() {
      if ( $('.svm_analysis_results').text().length > 0 ) {
        $('.svm_analysis_results').html('Error: cannot submit data');
      }
    });

  });
});
