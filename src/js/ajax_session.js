/**
 * ajax_session.js: this script utilizes ajax to retrieve data from
 *                  'retriever_session.py'. Specifically, the 'svm_title', and
 *                  'id_entity' values are taken from EAV data model, database
 *                  tables, and inserted into the DOM element 'svm_session_id'.
 */

// AJAX Process
  function session_id() {
    $.ajax({
      type: 'POST',
      url: '/retrieve-session/',
      dataType: 'json',
      beforeSend: function() {
        ajaxLoader( $('form') );
      }
    }).done(function(data) {

    // Remove AJAX Overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });

    // Append to DOM
      if (data.error) {
        $('.fieldset_dataset_type').append('<div class="error">' + data.error + '</div>');
        $('.fieldset_select_model').append('<div class="error">' + data.error + '</div>');
      }
      else {
        $.each( data, function( index, value ) {
          var value_id    = value['id'];
          var value_title = value['title'];
          var element     = '<option ' + 'value="' + value_id + '">' + value_title + '</option>';

          $('select[name="svm_session_id"]').append( element );
        });
      }

    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);

    // Remove AJAX Overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    });
  }
