console.log("Script connected!");

function check(checkbox, uncheck1, uncheck2) {
  // Uncheck other checkboxes in the same group
  $('input[name="' + checkbox.name + '"]').not(checkbox).prop('checked', false);
  
  // Uncheck checkboxes in the other group
  $('#' + uncheck1 + ',#' + uncheck2).prop('checked', false);
}

function combineOptions() {
  var options1 = $('input[name="group1"]:checked').val();
  var options2 = $('input[name="group2"]:checked').val();
  
  if (options1 && options2) {
    console.log('Selected options: ' + options1 + ', ' + options2);
  } else {
    console.log('Please select one option from each group.');
  }
}

