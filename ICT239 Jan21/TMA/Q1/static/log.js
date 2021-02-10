function calculate() {
    var weight = $('.weight').val();
    var walk = $('.walking').val();
    var run = $('.running').val();
    var swim = $('.swimming').val();
    var bike = $('.bicycling').val();
    var walkCal = 0;
    var runCal = 0;
    var swimCal = 0;
    var bikeCal = 0;
    var totalCal = 0
    
    debugger
    if (weight !== '0') {
      $('#weightError').attr('class', 'noWeightError')
      if (walk !== 0) {
        var walkCal = (0.084 * weight) * walk;
        
      }
      if (run !== 0) {
        var runCal = (0.21 * weight) * run;
        
      }
      if (swim !== 0) {
        var swimCal = (0.13 * weight) * swim;
        
      }
      if (bike !== 0) {
        var bikeCal = (0.064 * weight) * bike;
        
      }
      
      totalCal = walkCal + runCal + swimCal + bikeCal
      totalCal = Math.round(totalCal)
      $('.totalCalText').html("Total calories to be burned:  " + totalCal)
      
    } else {
      $('#weightError').attr('class', 'yesWeightError')
    }
  }