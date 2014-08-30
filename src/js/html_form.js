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
  $('form').on('click', '.add_element', delegator_callback);

/**
 * delegator_callback: callback used within 'delegator_form' listener.  It creates
 *                     additional form elements when the event listener is fired.
 *
 * @event.preventDefault, when this method is called, the default action of the
 *                     element will not be fired.
 */

  function delegator_callback(event) {
    event.preventDefault();
    console.log( $(this).prop('class') );
  }

});
