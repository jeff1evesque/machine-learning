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
    function(value, element) {
      var acceptable = ['value1', 'value2'];
      if ( $.inArray(value, acceptable) >= 0 ) {
        return true;
      }
      else return false;
    }, '');

// Validation: use the above 'definition'
  $(document).ready(function() {

    $('form').validate({
      rules: {
        svm_session: {
          equals: true
        }
      },
      messages: {
        svm_session: "That's not correct",
      },
    });
  });
