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


// function bmi(){

//     debugger
//     /* Using Javascript & DOM Selectors */ 
//     let height = document.getElementsByClassName("height_input")[0].value; /* https://www.w3schools.com/jsref/met_document_getelementsbyclassname.asp */
//     /* let feet = document.querySelector(".feet").value; */

//     /* Using Javascript & JQuery Selector */
//     let feet2 = $(".height_input")[0].value /* https://www.w3schools.com/jquery/jquery_ref_selectors.asp */

//     var clearBtn = document.getElementById("clear");
//     var calcBtn = document.getElementById("bmi");

//     if (clearBtn.getAttribute("usrOn") == "0") {
//         clearBtn.setAttribute("usrOn", "1")
//         /* store away original background color and opacity */
//         clearBtn.setAttribute("origC", getComputedStyle(clearBtn).backgroundColor);
//         clearBtn.setAttribute("origO", getComputedStyle(clearBtn).opacity);
//     } 

//     /* flip to calcBtn background color and opacity */
//     let color=calcBtn.getAttribute("origC");
//     let opacity=getComputedStyle(calcBtn).opacity;

//     // clearBtn.setAttribute("style", "background-color: " + color);
//     // Not advisable to do the above: https://www.w3schools.com/jsref/met_element_setattribute.asp 
//     clearBtn.style.backgroundColor=color;
//     clearBtn.style.opacity=opacity;

//     let weight = document.querySelector(".weight_input").value;

//     if (document.getElementById('m').checked) {
//         var bmi = weight / Math.pow(height, 2);      
//     } else {
//         var bmi = weight / Math.pow(height/100, 2);
//     }

//     debugger
//     if (document.querySelector(".output_space > p").innerHTML=="The Output Area") {
//         document.querySelector(".output_space > p").innerHTML=""
//     }

//     if (bmi < 18.5) {
//         document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Under Weight"+"<br>";
//     } else if ((bmi >= 25) && (bmi <= 29.9)) {
//         document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Over Weight"+"<br>";
//     } else if (bmi >= 30) {
//         document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Obesse"+"<br>";
//     } else {
//         document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value normal"+"<br>";
//     }
// }

function bmi(){

    debugger
    /* Using Javascript & DOM Selectors */ 
    let height = document.getElementsByClassName("height_input")[0].value; /* https://www.w3schools.com/jsref/met_document_getelementsbyclassname.asp */
    /* let feet = document.querySelector(".feet").value; */

    /* Using Javascript & JQuery Selector */
    let feet2 = $(".height_input")[0].value /* https://www.w3schools.com/jquery/jquery_ref_selectors.asp */

    var clearBtn = document.getElementById("clear");
    var calcBtn = document.getElementById("bmi");

    if (clearBtn.getAttribute("usrOn") == "0") {
        clearBtn.setAttribute("usrOn", "1")
        /* store away original background color and opacity */
        clearBtn.setAttribute("origC", getComputedStyle(clearBtn).backgroundColor);
        clearBtn.setAttribute("origO", getComputedStyle(clearBtn).opacity);
    } 

    /* flip to calcBtn background color and opacity */
    let color=calcBtn.getAttribute("origC");
    let opacity=getComputedStyle(calcBtn).opacity;

    // clearBtn.setAttribute("style", "background-color: " + color);
    // Not advisable to do the above: https://www.w3schools.com/jsref/met_element_setattribute.asp 
    clearBtn.style.backgroundColor=color;
    clearBtn.style.opacity=opacity;

    let weight = document.querySelector(".weight_input").value;

    if (document.getElementById('m').checked) {
        var aUnit = 'm'     
    } else {
        var aUnit = 'cm'
    }

    debugger
    if (document.querySelector(".output_space > p").innerHTML=="The Output Area") {
        document.querySelector(".output_space > p").innerHTML=""
    }

    $.ajax({
      url:"http://localhost:8000/bmi-ajax",
      type: "POST",
      data:{weight: weight,
      height: height,
      unit: aUnit},
      dataType: 'jsonp',   //you may use jsonp for cross origin request
      crossDomain: true,
      error: function() {
        alert("Error");
      },
      success: function(data, status, xhr) {
        var bmi = data.bmi
        debugger  
        if (bmi < 18.5) {
            document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Under Weight"+"<br>";
        } else if ((bmi >= 25) && (bmi <= 29.9)) {
            document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Over Weight"+"<br>";
        } else if (bmi >= 30) {
            document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value is Obesse"+"<br>";
        } else {
            document.querySelector(".output_space > p").innerHTML += "Your Body Mass Index (BMI) is: "+(Math.round(bmi*100/100)).toFixed(2)+"<br>"+" Index Value normal"+"<br>";
        }
    }})
}


function clear(){
    debugger
    document.querySelector(".output_space > p").innerHTML = "The Output Area";

    /* Restore Original Color and Opacity */
    this.setAttribute("usrOn", "0")
    let origO=this.getAttribute("origO")
    let origC=this.getAttribute("origC")

    /* These won't work for non-user defined attributes 
    this.setAttribute("opacity", origO);
    this.setAttribute("backgroundColor", origC);
    */
   this.style.backgroundColor=origC;
   this.style.opacity=origO;

   let inWeight = document.querySelector(".weight_input");
   /* inWeight.style.placeholder="kg" */
   inWeight.value=""
   /*document.querySelector(".weight").style.opacity=1;
   document.querySelector(".weight").style.backgroundColor="#FFFFFF";*/
   let inHeight = document.querySelector(".height_input"); 
   /* inHeight.style.placeholder="cm or m" */
   inHeight.value=""
   /*document.querySelector(".height").style.opacity=1;
   document.querySelector(".height").style.backgroundColor=rgb(255,255,255);*/
   let mButton=document.getElementById('m')
   let cmButton=document.getElementById('cm')
   if (mButton.checked == false) {
        cmButton.checked = false;
        mButton.checked = true;
   }
}

document.querySelector("#bmi").addEventListener("click", bmi);
document.querySelector("#clear").addEventListener("click", clear);