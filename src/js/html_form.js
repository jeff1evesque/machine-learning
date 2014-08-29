/**
 *  html_form.js: adds additional form elements to the DOM, when the user clicks
 *                'Add more'.
 *
 *                This script implements a 'delegation listener' which attaches a
 *                single event listener to a parent element, and fires for all
 *                descendants matching a selector.
 */

$(document).ready(function() {

// delegation listener
  $(body).on('click', '.add_element', delegator_callback(event));

/**
 * delegator_callback: callback used within 'delegator_form' listener.  It creates
 *                     additional form elements when the event listener is fired.
 */

  delegator_callback(e) {
    alert($(this).attr('class').split(' ')[1]));
  }

});
