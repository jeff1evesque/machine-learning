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
  // Local Variable
    var form_to_validate = $('form');

  // Validate
    $(form_to_validate).validate();

  // Count number of invalid fields
    $(form_to_validate).submit(function () {
      var validator = $(form_to_validate).validate();    
      var valid = $(form_to_validate).valid();
      var invalids = validator.numberOfInvalids();
    });
  });
