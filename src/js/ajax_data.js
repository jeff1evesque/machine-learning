/**
 * ajax_data.js: this script utilizes ajax to relay the form POST data, to a defined
 *               'action' script.
 */

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

  // Local Variables
    var form_data = new FormData();
    var dataset   = $('input[name="svm_dataset[]"]');
    var flag_ajax = true;

  // Serialize Data into Array (not file-uploads)
    var data_formatted = $('form').serializeArray();

  // Store 'file upload(s)' into Array
    if ( dataset.length > 0 && dataset.attr('type') == 'file' ) {
      $( dataset ).each(function( index ) {
        var file_data = dataset[index].files[0];
        form_data.append('file_upload_' + index, file_data);
      });
    }

  // Undefined 'file upload(s)' sets 'flag_ajax = false'
    dataset.each(function() {
      if ( typeof $(this).val() === 'undefined' ) {
        flag_ajax = false;
        return false
      }
    });

  // Combine 'form_data' (file-uploads) with 'data_formatted' (form data)
    var ajax_data = {properties: data_formatted, file_uploads: form_data};

  // AJAX Process
    if ( flag_ajax ) {
      $.ajax({
        url: $(this).attr('action'),
        type: 'POST',
        data: ajax_data,
        dataType: 'json',
        contentType: false,
        processData: false,
        beforeSend: function() {

        // AJAX Overlay
          ajaxLoader( $(event.currentTarget) );

        // Form Validation
          $("form").validate({
            submitHandler: function(form) {
              $(form).ajaxSubmit();
            }
          });

        }
      }).done(function(data) {

      // JSON Object from Server
        json_server = ( !$.isEmptyObject( data ) ) ? JSON.stringify(data, undefined, 2) : 'none';
        console.log( 'JSON object from Server: ' + json_server );

      // Remove AJAX Overlay
        $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });

      }).fail(function(jqXHR, textStatus, errorThrown) {
        console.log('Error Thrown: '+errorThrown);
        console.log('Error Status: '+textStatus);
      });
    }

  });
});
