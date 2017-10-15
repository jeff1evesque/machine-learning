/**
 * ajax-caller.js: an array of feature (independent variables) names, and the
 *                 generalized count of features that can be expected within an
 *                 observation, is inserted to respective DOM elements.
 *
 */

// import fetch polyfill
import 'whatwg-fetch';
import Promise from 'promise-polyfill';

// AJAX Process
function fetchCaller(callbackDone, callbackFail, args) {
  // add promise to window
  if (!window.Promise) {
    window.Promise = Promise;
  }

  // define fetch headers
  let fetchHeaders = {
    Accept: 'text/javascript',
    'Content-Type': args.contentType,
  };
  if (args.contentType === null || args.contentType === undefined) {
    fetchHeaders = {
      Accept: 'text/javascript',
    };
  }

  // ajax logic: the encapsulating function, utilizes this fetch api, to
  //             properly send data, to the corresponding endpoint.
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
    headers: fetchHeaders,
  }).then((response) => {
    if (response.ok) {
      // asynchronous callback
      response.json().then((data) => { callbackDone(data); });
    } else {
      // throw custom error
      const error = {
        statusText: response.statusText,
        status: response.status,
      };
      throw error;
    }
  }).catch((e) => {
    // asynchronous callback
    callbackFail(e.statusText, e.status);
  });
}

// indicate which class can be exported, and instantiated via 'require'
export default function ajaxCaller(callbackDone, callbackFail, args) {
  return fetchCaller(callbackDone, callbackFail, args);
}
