console.log("Script connected!");

var selectedOptions = []; // declare the array as a global variable

function check(checkbox, uncheck1, uncheck2) {
  // Uncheck other checkboxes in the same group
  $('input[name="' + checkbox.name + '"]').not(checkbox).prop('checked', false);

  // Uncheck checkboxes in the other group
  $('#' + uncheck1 + ',#' + uncheck2).prop('checked', false);
}

function combineDrinkOptions() {
  var options1 = $('input[name="group1"]:checked').val();
  var options2 = $('input[name="group2"]:checked').val();

  if (options1 && options2) {
    var combinedOptions = options1 + '(' + options2 + ') ';
    selectedOptions.push(combinedOptions);
    console.log('Selected options: ' + combinedOptions);
  } else {
    console.log('Please select one option from each group.');
  }

  // Uncheck all checkboxes
  $('input[type="checkbox"]').prop('checked', false);
}

function printDrinkOptions() {
  console.log('Selected options: ' + selectedOptions);
}
