/**
 * ajax_session.js: this script utilizes ajax to retrieve data from
 *                  'retriever_session.php'. Specifically, the 'svm_title', and
 *                  'id_entity' values are taken from EAV data model, database
 *                  tables, and inserted into the DOM element 'svm_session_id'.
 */

$(document).ready(function() {

// local variables
  var MutationObserver = window.MutationObserver || window.WebKitMutationObserver || window.MozMutationObserver;
  var container        = document.querySelector('form');
  var observer         = new MutationObserver(function(mutations) {

  mutations.forEach(function(mutation) {

    if ( mutation.type == 'childList' && typeof mutation.addedNodes == 'object' && mutation.addedNodes.length > 0 ) {

      for (var i=0; i < mutation.addedNodes.length; ++i) {
        var fieldset = mutation.addedNodes[i];

        if ( fieldset.nodeName !== '#text' ) {
          console.log("Recording mutation:", fieldset);
        }
      }

    }

  });
});

observer.observe(container, {
    attributes: true,
    attributeFilter: ['name'],
    childList: true,
    subtree: true,
    characterData: true
});



  $('select[name="svm_session"]').on('change', function(event) {
    event.preventDefault();







    if ( $('.fieldset_session_data_upload').length > 0 && $('select[name="svm_session_id"]').length > 0 ) {
    // AJAX Process
      $.ajax({
        type: 'POST',
        url: '../../php/retriever_sesion.php',
        dataType: 'json',
        beforeSend: function() {
          ajaxLoader( $(event.currentTarget) );
        }
      }).done(function(data) {

      // Append to DOM
        $.each( data['return'], function( index, value ) {
          var value_id    = value['value_id'];
          var value_title = value['value_title'];
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

  });
});
