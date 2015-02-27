/**
 * ajax_session.js: this script utilizes ajax to retrieve data from
 *                  'retriever_session.php'. Specifically, the 'svm_title', and
 *                  'id_entity' values are taken from EAV data model, database
 *                  tables, and inserted into the DOM element 'svm_session_id'.
 */

// AJAX Process
  function session_id() {
    $.ajax({
      type: 'POST',
      url: '../../php/retriever_session.php',
      dataType: 'json',
      beforeSend: function() {
        ajaxLoader( $('form') );
      }
    }).done(function(data) {

    // Append to DOM
      $.each( data, function( index, value ) {
        var value_id    = value['id'];
        var value_title = value['title'];
        var element     = '<option ' + 'value="' + value_id + '">' + value_title + '</option>';

        $('select[name="svm_session_id"]').append( element );

      // Remove AJAX Overlay
        $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
      })

    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);

    // Remove AJAX Overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    });
  }
