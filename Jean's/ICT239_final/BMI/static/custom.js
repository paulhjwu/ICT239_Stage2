

function bmi()
{
    console.log("In the function");

    //Get weight and height from the inputs

    //(1) getElementsByClassName
    let height = document.getElementsByClassName('height_input')[0].value;
    console.log(height);

    let weight = document.querySelector(".weight_input").value;
    console.log(weight);


    //check if m or cm is selected
    if (document.getElementById('m').checked)       // == true
    {
        //var bmi = weight / Math.pow(height, 2);     //BMI = mass/height (power2)
        var aUnit = 'm'
    }
    else
    {
       // var bmi = weight / Math.pow(height/100, 2);
       var aUnit = 'cm'
    }

    //Clear outtput text 
    if (document.querySelector(".output_space p").innerHTML == "The Output Area")
    {
        document.querySelector(".output_space p").innerHTML = ""
    }


    //Show bmi message in the output space
    /*if (bmi < 18.5) {
        document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is underweight.<br>";
    }
    else if ((bmi >= 18.5) && (bmi <= 29.9))
    {
        document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is normal.<br>";
    }
    else
    {
        document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is overweight.<br>";
    }*/


    //insert the ajax code here
    $.ajax({
        url:"/process",
        type:"POST",
        data: {weight: weight,
        height:height,
        unit: aUnit},
        error: function() {
            alert("Error");
        },
        success: function(data, status, xhr) {
            var bmi = data.bmi;
            console.log("bmi : " + bmi);

            //Show bmi message in the output space
            if (bmi < 18.5) {
                document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is underweight.<br>";
            }
            else if ((bmi >= 18.5) && (bmi <= 29.9))
            {
                document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is normal.<br>";
            }
            else
            {
                document.querySelector(".output_space p").innerHTML += "Your Body Mass Index (BMI) is " + (Math.round(bmi).toFixed(2)) + "<br> Index value is overweight.<br>";
            }

        }
    })



    // Flip clear button to same is the calculate button background color and opacity
    let clearBtn = document.getElementById("clear");
    let calcBtn = document.getElementById("bmi");
    
    if (clearBtn.getAttribute("usrOn") == "0")          //Clear button is off
    {
        clearBtn.setAttribute("usrOn", "1");             // Set clear button to on
        clearBtn.setAttribute("origC", getComputedStyle(clearBtn).backgroundColor);
        clearBtn.setAttribute("origO", getComputedStyle(clearBtn).opacity);
    }

    let color = calcBtn.getAttribute("origC");
    let opacity = getComputedStyle(calcBtn).opacity;

    clearBtn.style.backgroundColor = color;
    clearBtn.style.opacity = opacity;

}       //End of bmi function

function clear() {

    console.log("In clear function");

    document.querySelector(".output_space p").innerHTML = "The Output Area";

    /*Restore original color and opacity */
    this.setAttribute("usrOn", "0")
    let origO = this.getAttribute("origO");
    let origC = this.getAttribute("origC")

    this.style.backgroundColor = origC
    this.style.opacity = origO

    //clear inputs of weight and height
    document.querySelector(".weight_input").value = ""
    document.querySelector(".height_input").value = ""

    //let inWeight = document.querySelector(".weight_input");
   // inWeight = "";

    //let inHeight = document.querySelector(".height_input");
    //inHeight = "";



}



//add event listener for buttons, call event handling functions
document.querySelector("#bmi").addEventListener("click", bmi);
document.querySelector("#clear").addEventListener("click", clear)
