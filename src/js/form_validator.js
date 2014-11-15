/**
 * @form_validator.js: calls the 'validate()' method as suggested on per the
 *                     following documentation, and examples:
 *
 *     https://github.com/jzaefferer/jquery-validation#including-it-on-your-page
 *     http://jqueryvalidation.org/category/validator/
 */

/**
 * Definition: Compound Class Rules
 *
 * @parameter is the value passed in from the instantiating schema. For example,
 *     in `$('form').validate` (see below 'Validation:'), we have the key-value:
 *
 *         `equals: ['training', analysis']`
 *
 *     which is passed as an argument 'parameter' in this definition.
 */
  jQuery.validator.addMethod(
    'equals',
    function(value, element, parameter) {
      if ( $.inArray(value, parameter) >= 0 ) {
        return true;
      }
      else return false;
    }, '');

// Validation: use the above 'definition'
  $(document).ready(function() {

    $('form').validate({
      rules: {
        svm_session: {
          equals: ['training', 'analysis']
        }
      },
      messages: {
        svm_session: 'Not acceptable value',
      },
    });
  });
