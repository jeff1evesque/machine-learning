/**
 * ajax_data.js:
 */

$(document).ready(function() {
  $('form').on('submit', function(event) {
    event.preventDefault();

  // local variables
    var arr_data = new Array();

  // store 'file uploads' in array
    var dataset = $('input[name="svm_dataset[]"]');
    if ( dataset.length > 0 && dataset.attr('type') == 'file' ) {
      $( dataset ).each(function( index ) {
        arr_data.push( dataset.eq(index).prop('files'));
      });
      console.log(arr_data);
    }

  });
});
