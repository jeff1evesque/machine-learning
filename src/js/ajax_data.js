/**
 * ajax_data.js: this script utilizes ajax to relay the form POST data, to a defined
 *               'action' script.
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
 * Note: 'xml_upload(s)' is sent to python scripts via 'ajax_json.js'.
 *
 * Note: the implemented AJAX methods, and properties, are discussed more fully within
 *       'ajax_json.js'
 */

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

  // local variables
    var form_data = new FormData();
    var dataset   = $('input[name="svm_dataset[]"]');
    var flag_ajax = true;

  // store 'file upload(s)' in array
    if ( dataset.length > 0 && dataset.attr('type') == 'file' ) {
      $( dataset ).each(function( index ) {
        var file_data = dataset[index].files[0];
        form_data.append('file_upload_' + index, file_data);
      });
    }

  // undefined 'file upload(s)' sets 'flag_ajax = false'
    dataset.each(function() {
      if ( typeof $(this).val() === 'undefined' ) {
        flag_ajax = false;
        return false
      }
    });

  // ajax request: 'svm_dataset[]' file upload(s)
    if ( flag_ajax ) {
      $.ajax({
        url: '../../php/load_dataset.php',
        type: 'POST',
        data: form_data,
        dataType: 'json',
        contentType: false,
        processData: false,
      }).done(function(data) {
  // JSON object from Server
        json_server = ( !$.isEmptyObject( data ) ) ? JSON.stringify(data, undefined, 2) : 'none';
        console.log( 'JSON object from Server: ' + json_server );
      }).fail(function(jqXHR, textStatus, errorThrown) {
        console.log('Error Thrown: '+errorThrown);
        console.log('Error Status: '+textStatus);
      });
    }

  });
});

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

  // serialize data into array
    var data_formatted = $('form').serializeArray();

  // ajax request: form fields (except 'svm_dataset[]')
    $.ajax({
      url: $(this).attr('action'),
      type: 'POST',
      data : data_formatted,
      dataType : 'json',
      beforeSend: function() {

    // ajax overlay
        ajaxLoader( $(event.currentTarget) );

    // form validation
        $("form").validate({
          submitHandler: function(form) {
            $(form).ajaxSubmit();
          }
        });

      }
    }).done(function(data) {
  // JSON object from Server
      json_server = ( !$.isEmptyObject( data ) ) ? JSON.stringify(data, undefined, 2) : 'none';
      console.log( 'JSON object from Server: ' + json_server );

  // server side error
      $('form .fieldset_error').remove();
      if (data.hasOwnProperty('error')) {
        var msg_error = '\
            <fieldset class="fieldset_error">\
              <legend>Submission Error</legend>\
              <p>Error: '+data.result.error+'</p>\
            </fieldset>\
          ';
        $('form').prepend(msg_error);
      }

  // remove ajax overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    }).fail(function(jqXHR, textStatus, errorThrown) {
      $('form .fieldset_error').remove();

      var msg_error = '\
          <fieldset class="fieldset_error">\
              <legend>Submission Error</legend>\
              <p>Error: '+data.result.error+'</p>\
            </fieldset>\
          ';
        $('form').prepend(msg_error);
      }

  // remove ajax overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    }).fail(function(jqXHR, textStatus, errorThrown) {
      $('form .fieldset_error').remove();

      var msg_error = '\
          <fieldset class="fieldset_error">\
            <legend>Submission Error</legend>\
            <p>Error: '+errorThrown+'</p>\
          </fieldset>\
        ';
     $('form').prepend(msg_error);

      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);
    });

  });
});
