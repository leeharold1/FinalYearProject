console.log("Script connected!");

document.addEventListener('DOMContentLoaded', () => {
  const userID = document.getElementById('userID');
  const cleanID = userID.innerText;
  console.log(cleanID);
});

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

// function printDetails() {
//   console.log(userID.innerText + ' ' + selectedOptions);
// }

// function printDetails() {
//   var totalPrice = 0
//   var prices = selectedOptions.toString();
//   prices = prices.replace('Coke(330ml)', 1);
//   prices = prices.replace('7Up(500ml)', 1.75);
//   prices = prices.replace('Water(1L)', 2.50);
//   var convertedOptions = prices.split(",");
//   totalPrice = convertedOptions.join(", ");
//   console.log(totalPrice);
// }

function printDetails() {
  var totalPrice = 0
  var prices = selectedOptions.toString();
  for (let i = 0; i < selectedOptions.length; i++) {
    prices = prices.replace('Coke(330ml)', 1);
    prices = prices.replace('Coke(500ml)', 2);
    prices = prices.replace('Coke(1L)', 3);
    prices = prices.replace('7Up(330ml)', 1);
    prices = prices.replace('7Up(500ml)', 2);
    prices = prices.replace('7Up(1L)', 3);
    prices = prices.replace('Water(330ml)', 1);
    prices = prices.replace('Water(500ml)', 1.50);
    prices = prices.replace('Water(1L)', 2);
  }
  var convertedOptions = prices.split(",");
  totalPrice = convertedOptions.join(", ");
  for (let i = 0; i < totalPrice.length; i++) {
    totalPrice += totalPrice[i];
  }
  console.log(totalPrice);
}
