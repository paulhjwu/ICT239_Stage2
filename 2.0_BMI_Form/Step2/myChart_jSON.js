// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = 760 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

//Read the data
//var f = "Data35.csv";

var api = 'https://api.coindesk.com/v1/bpi/historical/close.json?start=2017-12-31&end=2018-04-01';

//api date is pass in as a JSON format

//Step 2: pass the data to a function which will return an array 
function parseData(data)
{
    //Retreive data and push into an array
    var arr = [];

    for (var i in data.bpi)
    {
      arr.push({ date: new Date(i),    //store in date format
                  value: +data.bpi[i]   //convert string to number
      })
    }

    return arr;

}

//Step 1 : use fetch method to get the data from the external API

fetch(api)
  .then((response) => {
      //The response that's returned will be in a JSON format
      return response.json();
  })
  .then((data) => {
      var parseMyData = parseData(data);      //store return JSON format file into an array variable
      drawChart(parseMyData)
  })


/*d3.csv(f,

  // When reading the csv, I must format variables:
  function(d){
    return { date : d3.timeParse("%Y-%m-%d")(d.date), value : d.value }
  }, */

  // Now I can use this dataset:
  //function(data) {

  function drawChart(data) {

    // Add X axis --> it is a date format
    var x = d3.scaleTime()
      .domain(d3.extent(data, function(d) { return d.date; }))
      .range([ 0, width ]);
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    // Add Y axis
    var y = d3.scaleLinear()
      .domain([0, d3.max(data, function(d) { return +d.value; })])
      .range([ height, 0 ]);
    svg.append("g")
      .call(d3.axisLeft(y));

    // Add the line
    svg.append("path")
      .datum(data)
      .attr("fill", "none")
      .attr("stroke", "steelblue")
      .attr("stroke-width", 1.5)
      .attr("d", d3.line()
        .x(function(d) { return x(d.date) })
        .y(function(d) { return y(d.value) })
        )

}
