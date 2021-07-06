

// function bmi()
// {
//     console.log("In the function");

//     //Get weight and height from the inputs

//     //(1) getElementsByClassName
//     let height = document.getElementsByClassName('height_input')[0].value;
//     console.log(height);

//     let weight = document.querySelector(".weight_input").value;
//     console.log(weight);


//     //check if m or cm is selected
//     if (document.getElementById('m').checked)       // == true
//     {
//         //var bmi = weight / Math.pow(height, 2);     //BMI = mass/height (power2)
//         var aUnit = 'm'
//     }
//     else
//     {
//        // var bmi = weight / Math.pow(height/100, 2);
//        var aUnit = 'cm'
//     }

//     debugger;
//     //Clear outtput text 
//     if (document.querySelector(".output_space p").innerHTML == "The Output Area")
//     {
//         document.querySelector(".output_space p").innerHTML = ""
//     }


//     //Show bmi message in the output space
//     /*if (bmi < 18.5) {
//         document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is underweight.<br>";
//     }
//     else if ((bmi >= 18.5) && (bmi <= 29.9))
//     {
//         document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is normal.<br>";
//     }
//     else
//     {
//         document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is overweight.<br>";
//     }*/

//     debugger;
//     // Flip clear button to same is the calculate button background color and opacity
//     let clearBtn = document.getElementById("clear");
//     let calcBtn = document.getElementById("bmi");
    
//     if (clearBtn.getAttribute("usrOn") == "0")          //Clear button is off
//     {
//         clearBtn.setAttribute("usrOn", "1");             // Set clear button to on
//         clearBtn.setAttribute("origC", getComputedStyle(clearBtn).backgroundColor);
//         clearBtn.setAttribute("origO", getComputedStyle(clearBtn).opacity);
//     }

//     let color = calcBtn.getAttribute("origC");
//     let opacity = getComputedStyle(calcBtn).opacity;

//     clearBtn.style.backgroundColor = color;
//     clearBtn.style.opacity = opacity;

//     //insert the ajax code here
//     $.ajax({
//         url:"/process",
//         type:"POST",
        
//         data: {weight: weight,
//         height:height,
//         unit: aUnit},

//         error: function() {
//             debugger
//             alert("Error");
//         },

//         success: function(data, status, xhr) {
//             var bmi = data.bmi;
//             console.log("bmi : " + bmi);
//             debugger;
//             //Show bmi message in the output space
//             if (bmi < 18.5) {
//                 document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is underweight.<br>";
//             }
//             else if ((bmi >= 18.5) && (bmi <= 29.9))
//             {
//                 document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is normal.<br>";
//             }
//             else
//             {
//                 document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is overweight.<br>";
//             }

//         }
//     })



// }       //End of bmi function

// function clear() {

//     console.log("In clear function");

//     document.querySelector(".output_space p").innerHTML = "The Output Area";

//     /*Restore original color and opacity */
//     this.setAttribute("usrOn", "0")
//     let origO = this.getAttribute("origO");
//     let origC = this.getAttribute("origC")

//     this.style.backgroundColor = origC
//     this.style.opacity = origO

//     //clear inputs of weight and height
//     document.querySelector(".weight_input").value = ""
//     document.querySelector(".height_input").value = ""

//     //let inWeight = document.querySelector(".weight_input");
//    // inWeight = "";

//     //let inHeight = document.querySelector(".height_input");
//     //inHeight = "";

// }



// //add event listener for buttons, call event handling functions
// document.querySelector("#bmi").addEventListener("click", bmi);
// document.querySelector("#clear").addEventListener("click", clear)


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
      url:"/process",
      type: "POST",
      data:{weight: weight,
      height: height,
      unit: aUnit},
    //   dataType: 'json',   //you may use jsonp for cross origin request
    //   crossDomain: true,
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