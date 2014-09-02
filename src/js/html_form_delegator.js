/**
 *  html_form_delegator.js: adds and removes additional form elements to the DOM,
 *                          when the user clicks either 'Add more', or 'Remove'.
 *
 *                          This script implements the jquery 'event delegation'
 *                          which attaches a single event listener to a parent
 *                          element, and fires for all descendants matching a
 *                          selector.
 */

$(document).ready(function() {

// local variables
  var element = {};


// delegation listeners
  $('form').on('click', '.add_element', add_callback);
  $('form').on('click', '.remove_element', remove_callback);

/**
 * add_callback: callback used within 'delegation listener'.  It creates additional
 *               form elements to be placed after the 'Remove' button, when the
 *               event listener is fired.
 *
 * @event.preventDefault, when this method is called, the default action of the
 *               element will not be fired.
 *
 * @grep(array, Boolean), discards nulls, undefineds, empty strings and integer 0's
 */

  function add_callback(event) {
    event.preventDefault();

    element.button_class = $(this).prop('class').trim().split(' ')[1];
    element.input_id = element.button_class.replace('_add', '');

    element.input_type = $('#'+element.input_id).attr('type');
    element.input_type_string = "type='"+element.input_type+"'";
    element.input_name = $('#'+element.input_id).attr('name');
    element.input_name_string = "name='"+element.input_name+"'";
    element.input_placeholder = $('#'+element.input_id).attr("placeholder");
    element.input_placeholder_string = "placeholder='"+element.input_placeholder+"'";
    element.input_arraySize = $("input["+element.input_name_string+"]").length;

  // Append element after 'Remove' button
    if (element.input_arraySize > 1) 
      $("input["+element.input_name_string+"]").last().after("<input "+ $.grep([element.input_type_string, element.input_name_string, element.input_placeholder_string], Boolean).join(', ') +">");
    else
      $('.'+element.input_id+'_remove').after("<input "+ $.grep([element.input_type_string, element.input_name_string, element.input_placeholder_string], Boolean).join(', ') +">");
  }

/**
 * remove_callback: callback used within a 'delegation listener'.  It removes the
 *                  last corresponding form element after a 'Remove' button within
 *                  the immediate 'fieldset', when the event listener is fired.
 *
 * @event.preventDefault, when this method is called, the default action of the
 *                  element will not be fired.
 */

  function remove_callback(event) {
    event.preventDefault();

    element.button_class = $(this).prop('class').trim().split(' ')[1];
    element.input_id = element.button_class.replace('_remove', '');
    element.input_name = $('#'+element.input_id).attr('name');
    element.input_arraySize = $('[name="'+element.input_name+'"]').length;

  // Remove last form element
    if (element.input_arraySize > 1) {
      $('input[name="'+element.input_name+'"]').last().remove();
    }
  }

});
