$(function(){

  $('#adds').on('click',add);
  $('#subs').on('click',remove);

});


function add(){

  var input = $('#noOfRoom'),
      value = input.val();

  input.val(++value);

  if(value > 3){
    $('#subs').removeAttr('disabled');
  }

}


function remove(){

   var input = $('#noOfRoom'),
       value = input.val();

   if(value > 3){
     input.val(--value);
   }else{
     $('#subs').attr('disabled','disabled');
  }

}
