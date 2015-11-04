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
  $('form').on('click', '.add-element', addCallback);
  $('form').on('click', '.remove-element', removeCallback);

  /**
   * addCallback: callback used within 'delegation listener'.  It creates additional
   *              form elements to be placed after the 'Remove' button, when the
   *              event listener is fired.
   *
   * @param {object} event.preventDefault, when this method is called, the default
   *     action of the element will not be fired.
   *
   * @param {function} grep(array, Boolean), discards nulls, undefineds, empty strings
   *     and integer 0's
   */

  function addCallback(event) {
    event.preventDefault();

    element.buttonClass            = $(this).prop('class').trim().split(' ')[1];
    element.inputId                = element.buttonClass.replace('-add', '');
    element.inputClassString       = (element.inputId !== undefined) ? 'class=\'' + element.inputId + '\'' : null;

    element.inputType              = (element.inputId !== undefined) ? $('.' + element.inputId).attr('type') : null;
    element.inputTypeString        = (element.inputType !== undefined) ? 'type=\'' + element.inputType + '\'' : null;

    element.inputName              = (element.inputId !== undefined) ? $('.' + element.inputId).attr('name') : null;
    element.inputNameString        = (element.inputName !== undefined) ? 'name=\'' + element.inputName + '\'' : null;

    element.inputPlaceholder       = (element.inputId !== undefined) ? $('.' + element.inputId).attr('placeholder') : null;
    element.inputPlaceholderString = (element.inputPlaceholder !== undefined) ? 'placeholder=\'' + element.inputPlaceholder + '\'' : null;

    element.inputArraySize         = $('input[' + element.inputNameString + ']').length;

    // Append element after 'Remove' button
    if (element.inputArraySize > 1)
      $('input[' + element.inputNameString + ']').last().after('<input ' + $.grep([element.inputTypeString, element.inputNameString, element.inputPlaceholderString, element.inputClassString], Boolean).join(', ') + '>');
    else
      $('.' + element.inputId + '-remove').after('<input ' + $.grep([element.inputTypeString, element.inputNameString, element.inputClassString, element.inputPlaceholderString], Boolean).join(', ') + '>');

    // Remove fieldset 'dependencies'
    $(this).parent().nextAll().remove();

    // Remove 'submit' button
    $('.svm-form-submit').remove();
  }

  /**
   * removeCallback: callback used within a 'delegation listener'.  It removes the
   *                 last corresponding form element after a 'Remove' button within
   *                 the immediate 'fieldset', when the event listener is fired.
   *
   * @param {object} event.preventDefault, when this method is called, the default
   *                 action of the element will not be fired.
   */

  function removeCallback(event) {
    event.preventDefault();

    element.buttonClass    = $(this).prop('class').trim().split(' ')[1];
    element.inputId        = element.buttonClass.replace('-remove', '');
    element.inputName      = $('.' + element.inputId).attr('name');
    element.inputArraySize = $('[name="' + element.inputName + '"]').length;

    // Remove last form element
    if (element.inputArraySize > 1) {
      $('input[name="' + element.inputName + '"]').last().remove();
    }
  }

});
