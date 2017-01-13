/**
 * ajax_caller.js: an array of feature (independent variables) names, and the
 *                 generalized count of features that can be expected within an
 *                 observation, is inserted to respective DOM elements.
 *
 */

// AJAX Process
function ajaxCaller(callbackDone, callbackFail, args) {
  // define fetch headers
  var fetchHeaders = {
    'Accept': 'text/javascript',
    'Content-Type': args.contentType
  };
  if (args.contentType === null || args.contentType === undefined) {
    fetchHeaders = {
      'Accept': 'text/javascript'
    };
  }

  // ajax logic: generalized function that can be imported, and implemented.
  //
  // Note: in order to better understand header responses, with respect to the
  //       fetch api, the following can be reviewed:
  //
  //       https://[github-url]/issues/2863#issuecomment-272355998
  //
  fetch(args.endpoint, {
    method: 'post',
    body: args.data,
    credentials: 'include',
    headers: fetchHeaders
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
