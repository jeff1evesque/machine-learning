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
  $('form input').on('click', '.add_element', delegator_callback);

/**
 * delegator_callback: callback used within 'delegator_form' listener.  It creates
 *                     additional form elements when the event listener is fired.
 */

  function delegator_callback(event) {
    console.log( $(this).prop('class') );
  }

});
