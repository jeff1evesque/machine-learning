/**
 * ajax_model.js: this script utilizes ajax to retrieve data from
 *                'retriever_model.py'. Specifically, every 'svm_model' is
 *                returned.
 */

// AJAX Process
  function model_id() {
    $.ajax({
      type: 'POST',
      url: '/retrieve-model/',
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
      }
      else {
        $.each( data, function( index, value ) {
          var value_id    = value['id'];
          var value_title = value['title'];
          var element     = '<option ' + 'value="' + value_id + '">' + value_title + '</option>';

          $('select[name="svm_model_id"]').append( element );
        });
      }

    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error Thrown: '+errorThrown);
      console.log('Error Status: '+textStatus);

    // Remove AJAX Overlay
      $('form .ajax_overlay').fadeOut(200, function(){ $(this).remove() });
    });
  }
