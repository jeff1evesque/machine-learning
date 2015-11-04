/**
 * @form_validator.js: call 'validate()' method on defined form elements.
 *
 *     http://jqueryvalidation.org/documentation/
 *     http://jqueryvalidation.org/category/validator/
 *     http://jqueryvalidation.org/jQuery.validator.addMethod/
 *     http://stackoverflow.com/questions/10843399#answer-10843593
 */

/**
 * Custom Method: callback function(s) used from the 'Compound Class Rules',
 *                and the 'Validation' sections (see below).
 *
 * @param {string} value, the value submitted on the given form element
 *
 * @param {string} element, the element being validated
 *
 * @param {string} parameter, additional parameters from the instantiating schema.
 *     For example, the 'validate' method (see below 'Validation:'), provides an
 *     array as a parameter to the added method 'equals':
 *
 *         `equals: ['training', 'analysis']`
 */
  jQuery.validator.addMethod(
    'equals',
    function(value, element, parameter) {
      if ($.inArray(value, parameter) >= 0) {
        return true;
      } else {
        return false;
      }
    });
jQuery.validator.addMethod(
  'integerOnly',
    function(value, element, parameter) {
      if (Math.round(parseInt(value)) === parseInt(value)) {
        return true;
      } else {
        return false;
      }
    });
jQuery.validator.addMethod(
  'numericOnly',
    function(value, element, parameter) {
    // invalid condition: -0, and -0.0
    if (value.match(/^-0*.0*$/)) {
      return false;
    }
    // validate integers: cannot start with 0 (except trivial 0)
    else if (value.match(/^-?(0|[1-9][0-9]*)$/)) {
      return true;
  // validate floats: cannot start with 0 (except trivial 0.x)
    } else if (value.match(/^-?(0|[1-9][0-9]*)?\.\d+$/)) {
      return true;
  // invalid condition: general
    } else {
      return false;
    }
  });
jQuery.validator.addMethod(
  'textOnly',
    function(value, element, parameter) {
      if (typeof(value) === 'string') {
        return true;
      } else {
        return false;
      }
    });
jQuery.validator.addMethod(
  'fileExtension',
    function(value, element, parameter) {
      if ($.inArray(element.files[0].name.split('.').pop().toLowerCase(), parameter) >= 0) {
        return true;
      } else {
        return false;
      }
    },
    'Incorrect file format'
  );

/**
 * Compound Class Rules: validates form elements by respective classnames.
 *                       This validation may implement the 'Definition(s)',
 *                       defined from the '.addMethod' definition.
 *
 * Note: These rules cannot define custom messages. Instead, the custom messages
 *       must be defined as the last parameter to the 'addMethod' definition (see
 *       above 'fileExtension').
 */
jQuery.validator.addClassRules({
    'svm-dataset-xml': {
      url: true,
    },
    'svm-dataset-file': {
      fileExtension: ['csv', 'xml', 'json'],
    },
  });

/**
 * Validation: validates form elements by the 'name' attribute. This validation
 *             may implement the 'Definition(s)', defined from the 'addmethod'
 *             definition.
 */
$(document).ready(function() {

  $('form').validate({
      rules: {
        svmSession: {
          required: true,
          equals: ['data_new', 'data_append', 'model_predict', 'model_generate']
        },
        svmTitle: {
          required: true,
          textOnly: true
        },
        svmSessionId: {
          required: true,
          integerOnly: true
        },
        svmModelId: {
          required: true,
          integerOnly: true
        },
        svmDatasetType: {
          required: true,
          equals: ['file_upload', 'dataset_url']
        },
        svmModelType: {
          required: true,
          equals: ['classification', 'regression']
        },
        'predictionInput[]': {
          required: true,
          numericOnly: true
        },
      },
      messages: {
        svmSession: 'Not valid value',
        svmTitle: 'Must be nonempty string',
        svmDatasetType: 'Not valid value',
        svmSessionId: 'Not valid value',
        svmModelType: 'Not valid value',
        'predictionInput[]': 'Must be valid nonempty decimal',
      },
    });
});
