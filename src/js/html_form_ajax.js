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
 * @ajaxLoader(), is defined within 'ajax_loader.js'.
 */

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

    $.ajax({
      url: $(this).attr('action'),
      type: 'POST',
      data: $(this).serialize(),
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
