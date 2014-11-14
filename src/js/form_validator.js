/**
 * @form_validator.js: this script calls the 'validate()' method as suggested on
 *                     the github documentation:
 *
 *     https://github.com/jzaefferer/jquery-validation#including-it-on-your-page
 */

// Compound Class Rules
  $.validator.addClassRules({

  });

// Validate HTML
$(document).ready(function() {
  $("form").validate();
});
