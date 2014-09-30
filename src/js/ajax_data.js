/**
 * ajax_data.js: this script utilizes ajax to relay the form POST data, specifically,
 *               'file uploads' to a defined 'action' script.
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

  // store 'file uploads' in array
    var dataset = $('input[name="svm_dataset[]"]');
    if ( dataset.length > 0 && dataset.attr('type') == 'file' ) {
      $( dataset ).each(function( index ) {
        var file_data = dataset.eq(index).prop('files')[0];
        form_data.append('file', file_data);
        arr_data.push( form_data );
      });
      console.log(arr_data);
    }

  // ajax request: 'svm_dataset[]' file upload(s)
    $.ajax({
      url: '../../php/load_dataset.php',
      type: 'POST',
      data: arr_data,
    }).done(function(data) {
      console.log('Success: data upload');
    }).fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Fail: data upload');
    });

  });
});
