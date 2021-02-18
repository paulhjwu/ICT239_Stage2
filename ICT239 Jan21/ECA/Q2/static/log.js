function postdata() { 
  debugger
  var weight = $('.weight').val();
  var walk = $('.walking').val();
  var run = $('.running').val();
  var swim = $('.swimming').val();
  var bike = $('.bicycling').val();
  var dt = $('.datetime').val();
  debugger
  $.ajax({
  url:"http://127.0.0.1:5000/log",
  method: "POST",
  data:{weight: weight,
  walk: walk,
  run: run,
  datetime: dt,
  swim: swim,
  bike: bike}
  }).done(function(data){
    debugger
    $('.totalCalText').html("Total calories to be burned:  " + data.calorie)
  }
  )
};