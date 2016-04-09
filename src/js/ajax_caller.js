/**
 * ajax_caller.js: an array of feature (independent variables) names, and the
 *                 generalized count of features that can be expected within an
 *                 observation, is inserted to respective DOM elements.
 */

// AJAX Process
function ajaxCaller(callbackDone, callbackFail, args) {
  // define fetch headers
  if (args.contentType === null || args.contentType == undefined) {
    var headers = {
      'Accept': 'text/javascript'
    };
  } else {
    var headers = {
      'Accept': 'text/javascript',
      'Content-Type': args.contentType
    };
  }

  // ajax logic
  fetch(args.endpoint, {
    method: 'post',
    body: args.data,
    headers: headers
  }).then(function(response) {
    if (response.ok) {
      // asynchronous callback
      response.json().then(function(data) { callbackDone(data); });
    } else {
      // throw custom error
      var error = {
        'statusText': response.statusText,
        'status': response.status
      };
      throw error;
    }
  }).catch(function(e) {
    // asynchronous callback
    callbackFail(e.statusText, e.status);
  });
}
