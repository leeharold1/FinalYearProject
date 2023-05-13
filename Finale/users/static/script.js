console.log("Script connected!");

var selectedOptions = []; // declare the array as a global variable

function check(checkbox, uncheck1, uncheck2) {
  // Uncheck other checkboxes in the same group
  $('input[name="' + checkbox.name + '"]').not(checkbox).prop('checked', false);

  // Uncheck checkboxes in the other group
  $('#' + uncheck1 + ',#' + uncheck2).prop('checked', false);
}

function updateDrinkAndPrice() {
  var options1 = $('input[name="group1"]:checked').val();
  var options2 = $('input[name="group2"]:checked').val();
  var combinedOptions = '';

  if (options1 && options2) {
    combinedOptions = options1 + '(' + options2 + ') ';
    selectedOptions.push(combinedOptions);
    console.log('Selected options: ' + combinedOptions);
  } else {
    console.log('Please select one option from each group.');
  }

  // Update the content of the <div> element with the combinedOptions
  $('#combinedOptionsDisplay').text('Added to Cart: ' + combinedOptions);

  var totalPrice = 0;
  var prices = selectedOptions.toString();
  for (let i = 0; i < selectedOptions.length; i++) {
    prices = prices.replace('Coke(330ml)', 1.30);
    prices = prices.replace('Coke(500ml)', 2.25);
    prices = prices.replace('Coke(1L)', 3.30);
    prices = prices.replace('7Up(330ml)', 1.30);
    prices = prices.replace('7Up(500ml)', 2.25);
    prices = prices.replace('7Up(1L)', 3.30);
    prices = prices.replace('Water(330ml)', 1);
    prices = prices.replace('Water(500ml)', 1.50);
    prices = prices.replace('Water(1L)', 2);
  }
  var convertedOptions = prices.split(",");
  totalPrice = eval(convertedOptions.join("+ "));

  // Set the totalPrice as the value for the price field
  document.getElementById("id_price").value = totalPrice.toFixed(2);

  // Set the combinedOptions as the value for the order field
  document.getElementById("id_order").value = selectedOptions;

  // Set the combinedOptions as the value for the order field
  document.getElementById("id_order").value = selectedOptions;

  // Uncheck all checkboxes
  $('input[type="checkbox"]').prop('checked', false);
}

function clearCart() {
  // Reset the selected options array
  selectedOptions = [];

  // Reset the combined options display
  $('#combinedOptionsDisplay').text('');

  // Reset the price field
  document.getElementById("id_price").value = '';

  // Reset the order field
  document.getElementById("id_order").value = '';

  // Uncheck all checkboxes
  $('input[type="checkbox"]').prop('checked', false);
}



