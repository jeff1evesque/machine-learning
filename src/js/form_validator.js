/**
 * @form_validator.js: calls the 'validate()' method as suggested on per the
 *                     following documentation, and examples:
 *
 *     https://github.com/jzaefferer/jquery-validation#including-it-on-your-page
 *     http://jqueryvalidation.org/category/validator/
 */

// Definition: Compound Class Rules
  jQuery.validator.addMethod(
    'equals',
    function(value, element, param) {
      return this.optional(element) || $.inArray(value, param) > 0;
    },
    jQuery.format('')
  );

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
