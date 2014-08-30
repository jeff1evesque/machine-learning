/**
 *  html_form.js: adds additional form elements to the DOM, when the user clicks
 *                'Add more'.
 *
 *                This script implements a 'delegation listener' which attaches a
 *                single event listener to a parent element, and fires for all
 *                descendants matching a selector.
 */

$(document).ready(function() {

// local variables
  var element = {};


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
    element['button_class'] = $(this).prop('class').split(' ')[1];
    element['input_id'] = element['button_class'].replace('_add', '');
    element['input_type'] = $('#'+element['input_id']).attr('type');
    element['input_name'] = $('#'+element['input_id']).attr('name');
    element['input_placeholder'] = $('#'+element['input_id']).attr("placeholder");

    $('.'+element['button_class']).after("<br><input type='"+element['input_type']+"' name='"+element['input_name']+"' placeholder='"+element['input_placeholder']+"'>");
  }

});
