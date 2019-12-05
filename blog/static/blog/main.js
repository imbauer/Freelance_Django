function increaseValue() {
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 2 : value;
  value++;
  document.getElementById('number').value = value;
  document.getElementById('dynamic').innerHTML = value;
}

function decreaseValue() {
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 2 : value;
  value < 3 ? value = 3 : '';
  value--;
  document.getElementById('number').value = value;
  document.getElementById('dynamic').innerHTML = value;
}
