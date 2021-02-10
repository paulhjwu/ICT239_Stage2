function postdata() { 
  debugger
  var weight = $('.weight').val();
  var walk = $('.walking').val();
  var run = $('.running').val();
  var swim = $('.swimming').val();
  var bike = $('.bicycling').val();
  debugger
  $.ajax({
  url:"/log",
  type: "POST",
  data:{weight: weight,
  walk: walk,
  run: run,
  swim: swim,
  bike: bike}, 
  error: function(xhr) {
    debugger
    alert('Request Status: ' + xhr.status + ' Status Text: ' + xhr.statusText + ' ' + xhr.responseText);
  },
  success: function(data, status, xhr) {
    var calorie = data.calorie;
    debugger
    $('.totalCalText').html("Total calories to be burned:  " + calorie);
  }}
  )
}