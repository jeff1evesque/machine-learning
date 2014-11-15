/**
 * @form_validator.js: call 'validate()' method on defined form elements.
 *
 *     http://jqueryvalidation.org/documentation/
 *     http://jqueryvalidation.org/category/validator/
 *     http://jqueryvalidation.org/jQuery.validator.addMethod/
 */

/**
 * Definition: Compound Class Rules
 *
 * @value the value submitted on the given form element
 *
 * @element the element being validated
 *
 * @parameter additional parameters from the instantiating schema. For example,
 *     the 'validate' method (see below 'Validation:'), provides an array as a
 *     parameter to the added method 'equals':
 *
 *         `equals: ['training', 'analysis']`
 */
  jQuery.validator.addMethod(
    'equals',
    function(value, element, parameter) {
      if ( $.inArray(value, parameter) >= 0 ) return true;
      else return false;
    });
  jQuery.validator.addMethod(
    'textOnly',
    function(value, element, parameter) {
      if ( typeof(value) === 'string' ) return true;
      else return false;
  });

// Validation: use the above 'definition'
  $(document).ready(function() {

    $('form').validate({
      rules: {
        svm_session: {
          equals: ['training', 'analysis']
        },
        svm_dataset_type: {
          equals: ['upload file', 'xml file']
        },
        svm_model_type: {
          equals: ['classification', 'regression']
        },
        'svm_indep_variable[]': {
          textOnly: true,
          minlength:1,
        }        
      },
      messages: {
        svm_session: 'Not acceptable value',
        svm_dataset_type: 'Not acceptable value',
        svm_model_type: 'Note acceptable value',
        'svm_indep_variable[]': 'Must be type string',
      },
    });
  });
