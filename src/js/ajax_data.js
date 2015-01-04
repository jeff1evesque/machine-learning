/**
 * ajax_data.js: this script utilizes ajax to relay the form POST data, to a defined
 *               'action' script.
 */

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

  // Local Variables
    var dataset   = $('input[name="svm_dataset[]"]');
    var flag_ajax = true;

  // Undefined 'file upload(s)' sets 'flag_ajax = false'
    dataset.each(function() {
      if ( typeof $(this).val() === 'undefined' ) {
        flag_ajax = false;
        return false
      }
    });

  // AJAX Process
    if ( flag_ajax ) {
      $.ajax({
        url: $(this).attr('action'),
        type: 'POST',
        data: new FormData( this ),
//        dataType: 'json',
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
