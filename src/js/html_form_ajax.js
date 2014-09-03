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
 */

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();
    var svm_feedback;

    $.ajax({
      url: $(this).attr('action'),
      type: 'POST',
      data: $(this).serialize(),
      beforeSend: function() {
        if ( $('.svm_analysis_results').text().length > 0 ) {
          var svm_feedback = $('.svm_analysis_results').text();
          $('.svm_analysis_results').html('sending...');
        }
      },
      success: function(data) {
        if ( $('.svm_analysis_results').text().length > 0 ) {
          $('.svm_analysis_results').html(svm_feedback);
        }
      },
      error: function() {
        if ( $('.svm_analysis_results').text().length > 0 ) {
          $('.svm_analysis_results').html('Error: cannot submit data');
        }
      }
    });
  });
});
