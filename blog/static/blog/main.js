function increaseValue() {
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 2 : value;
  value++;
  document.getElementById('number').value = value;
  var count = 24.90 + (4.95 * (value - 3))
  var count = count.toString();
  var numarray = count.split('.')
  document.getElementById('dynamic').innerHTML = count;
}

function decreaseValue() {
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 3 : value;
  value < 3 ? value = 3 : '';
  value--;
  document.getElementById('number').value = value;
  document.getElementById('dynamic').innerHTML = value;
}
