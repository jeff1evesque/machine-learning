/**
 * ajax_session.js: this script utilizes ajax to retrieve data from
 *                  'retriever_session.php'. Specifically, the 'svm_title', and
 *                  'id_entity' values are taken from EAV data model, database
 *                  tables, and inserted into the DOM element 'svm_session_id'.
 */

$(document).ready(function() {

// local variables
  var flag_ajax        = false;
  var MutationObserver = window.MutationObserver || window.WebKitMutationObserver || window.MozMutationObserver;
  var target           = document.querySelector('form');

// Mutation Observation: create observer instance
  var observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutation) {

      if ( mutation.type == 'childList' && typeof mutation.addedNodes == 'object' && mutation.addedNodes.length > 0 ) {
        for (var i=0; i < mutation.addedNodes.length; ++i) {
          var data_upload_container = mutation.addedNodes[i];

          if ( data_upload_container.nodeName !== '#text' ) {
            for (var j=0; j < data_upload_container.childNodes.length; ++j) {
              var data_upload_elements = data_upload_container.childNodes[j];

              if ( data_upload_elements.nodeName !== '#text' ) {
                for (var k=0; k < data_upload_elements.childNodes.length; ++k) {
                  var configuration_elements = data_upload_elements.childNodes[k];

                  if ( configuration_elements.nodeName.toLowerCase() === 'select' ) {
                    var attr_name = configuration_elements.name;
                    if ( attr_name === 'svm_session_id' ) {
                      flag_ajax = true;
                    }
                  }
                }
              }
            }
          }
        }
      }

    });
  });

// Mutation Observation: configuration for observer
  var config = { attributes: true, childList: true, subtree: true };

// Mutation Observation: pass target, and configuration to observer
  observer.observe(target, config);

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
