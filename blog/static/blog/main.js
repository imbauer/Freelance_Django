function increaseValue() {
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 4 : value;
  value++;
  document.getElementById('number').value = value;
  var count = 24.90 + (4.95 * (value - 3))
  var count = count.toString();
  var numarray = count.split('.')
  var a=new Array();
  a=numarray;
  if (a[1] === undefined) {
      a[1] = "00";
  }
  a[1] = "." + a[1];
  document.getElementById('dynamic').innerHTML = a[0];
  document.getElementById('dynamicdec').innerHTML = "." + parseFloat(a[1]).toFixed(2).toString().slice(-2);
  var input = document.getElementById("cost");
  input.value = value.toString() + ".00";
  console.log(input.value);
}

function decreaseValue() {
  var value = parseInt(document.getElementById('number').value, 10);
  value = isNaN(value) ? 4 : value;
  value < 4 ? value = 4 : '';
  value--;
  document.getElementById('number').value = value;
  var count = 24.90 + (4.95 * (value - 3))
  var count = count.toString();
  var numarray = count.split('.')
  var a=new Array();
  a=numarray;
  if (a[1] === undefined) {
      a[1] = "00";
  }
  a[1] = "." + a[1];
  document.getElementById('dynamic').innerHTML = a[0];
  document.getElementById('dynamicdec').innerHTML = "." + parseFloat(a[1]).toFixed(2).toString().slice(-2);
}
