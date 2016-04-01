/**
 * ajax_caller.js: an array of feature (independent variables) names, and the
 *                 generalized count of features that can be expected within an
 *                 observation, is inserted to respective DOM elements.
 */

// AJAX Process
function ajaxCaller(callbackDone, callbackFail, args) {
  // tell jquery to set the contentType
  if (args.contentType === null) {
    args.contentType = 'application/x-www-form-urlencoded; charset=UTF-8';
  }

  // tell jquery to process the data
  if (args.processData === null) {
    args.processData = true;
  }

  // ajax logic
  fetch(args.endpoint, {
    method: 'post',
    body: args.data,
    headers: {
      'Content-Type':  args.contentType
    }
  }).then(function(response) {
    if (response.ok) {
      // asynchronous callback
      callbackDone(response.json());
    } else {
      // throw custom error
      var error = {
        'statusText': response.statusText,
        'status': response.status,
        'headers': response.headers
	  }
      throw error;
    }
  }).catch(function(e) {
    // variables
    var serverResponse = (e.headers) ? e.headers : 'no server response';
    // asynchronous callback
    callbackFail(e.statusText, e.status);
  });
}
