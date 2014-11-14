/**
 * @form_validator.js: this script calls the 'validate()' method as suggested on
 *                     the github documentation:
 *
 *     https://github.com/jzaefferer/jquery-validation#including-it-on-your-page
 */

// Definition: Compound Class Rules
  $.validator.addClassRules({

  });

// Validation: use the above 'definition'
  $(document).ready(function() {
  // Validate
    $("form").validate();

  // Count number of invalid fields
    $('form').submit(function () {
      var validator = $('#testForm').validate();    
      var valid = $('#testForm').valid();
      var invalids = validator.numberOfInvalids();
    });
  });
