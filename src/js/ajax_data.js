/**
 * ajax_data.js: this script utilizes ajax to relay the form POST data, specifically,
 *               'file uploads' to a defined 'action' script.
 *
 * @contentType, the content type, some refer to as the 'MIME', is used when sending
 *    data to the server. The Default is 'application/x-www-form-urlencoded'. Setting
 *    this attribute to 'false', forces jQuery not to add a 'Content-Type' header. This
 *    property tells the browser, or server, how to open the specified file. 
 *
 * @processData, boolean value specifying whether or not data sent to server should be
 *   transformed into a query string.  The default is 'true'.  Setting this value to
 *   'false' tells jQuery not to convert the 'data' object into a serialized parameter
 *   string, which would be done before sending the 'data' to the server.
 *
 * Note: the implemented AJAX methods, and properties, are discussed more fully within
 *       'ajax_json.js'
 */

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

  // local variables
    var arr_data = new Array();
    var form_data = new FormData();
    var dataset = $('input[name="svm_dataset[]"]');

  // store 'file uploads' in array
    if ( dataset.length > 0 && dataset.attr('type') == 'file' ) {
      $( dataset ).each(function( index ) {
        var file_data = dataset.eq(index).prop('files')[0];
        form_data.append('file_data_' + index, file_data);
        arr_data.push( form_data );
      });
      console.log(arr_data);
    }

  // ajax request: 'svm_dataset[]' file upload(s)
    $.ajax({
      url: '../../php/load_dataset.php',
      type: 'POST',
      data: arr_data,
      contentType: false,
      processData: false,
    }).done(function(data) {
      console.log('Success: data upload ' + data);
    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Fail: data upload');
    });

  });
});
