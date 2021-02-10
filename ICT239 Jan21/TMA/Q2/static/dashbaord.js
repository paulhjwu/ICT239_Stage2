const STROKES = ["purple", "green", "black", "red",  "brown"];

// Get the today's date as "YYYY-MM-DD" string

let chart_date = new Date();
const offset = chart_date.getTimezoneOffset();
chart_date = new Date(chart_date.getTime() - (offset*60*1000));
chart_date = chart_date.toISOString().split('T')[0];

// Fetch the data and plot the chart
debugger
fetch(`/api/recordings?date=${chart_date}`).then(response => {
    debugger
    if (response.status === 200) {
        return response.json();
    } else {
        return Promise.reject();
    }
}).then(data => {
    debugger
    let recordings = data.recordings; // format: [{user_id: x, datetime: y, calorie: z}, ...]

    // Reformat the data for plotting chart

    let chart_data = {}; // format: {x: [{datetime: y, calorie: z}, ...], ...}
    let calories = []; // format: [z, ...]
    let dates = [];
    for (let recording of recordings) {
        if (!(recording.user_id in chart_data)) {
            chart_data[recording.user_id] = [];
        }

        chart_data[recording.user_id].push({
            datetime: new Date(recording.datetime),
            calorie: parseFloat(recording.calorie),
        });

        calories.push(recording.calorie);
        dates.push(new Date(recording.datetime))
    }

    // Sort the chart data by datetime
    
    for (const user_id in chart_data) {
        chart_data[user_id].sort((a, b) => a.datetime - b.datetime);
    }

    // Render and plot the chart

    const margin = { top: 20, right: 20, bottom: 30, left: 50 };
    const width = 660 - margin.left - margin.right;
    const height = 350 - margin.top - margin.bottom;

    /*
    debugger
    // Add X axis --> it is a date format
    var x = d3.scaleTime()
      .domain(d3.extent(dates).
      range([ 0, width ]);
    
    debugger
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x).tickFormat(d3.timeFormat("%Y-%m-%d")))
      .selectAll("text")	
      .style("text-anchor", "end")
      .attr("dx", "-.8em")
      .attr("dy", ".15em")
      .attr("transform", "rotate(-65)");

    // Add Y axis
    var y = d3.scaleLinear()
      .domain([0, d3.max(chart_data, function(d) { return +d.calorie; })])
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
    */
    
    debugger
    const today_date = new Date().setHours(0, 0, 0, 0);
    const x = d3.scaleTime().range([0, width])
        .domain(d3.extent(dates)).nice()
        //.domain([today_date - (24 * 60 * 60 * 1000), today_date])
        //.nice()et count = 0;

    const y = d3.scaleLinear().range([height, 0])
        .domain([d3.min(calories), d3.max(calories)])

    const svg_legend = d3.select("#chart-legend").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", 50)
    .append("g")
    .attr("transform",
        "translate(" + margin.left + "," + margin.top + ")");

    const svg = d3.select("#chart").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

    // Add the X Axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    // Add the Y Axis
    svg.append("g")
        .call(d3.axisLeft(y));

    // Plot the data on the chart
    let count = 0;
    for (let user_id in chart_data) {
        const valueline = d3.line()
            .x(d => x(d.datetime))
            .y(d => y(d.calorie));

        debugger 
        svg.append("path")
            .data([chart_data[user_id]])
            .attr("fill", "none")
            .attr("stroke-width", 1.5)
            .attr("class", "line")
            .style("stroke", STROKES[count % STROKES.length])
            .attr("d", valueline);

        svg_legend.append("circle")
            .attr("cx", 30 + count * 150)
            .attr("cy", 20)
            .attr("r", 6)
            .style("fill", STROKES[count % STROKES.length]);
        
        svg_legend.append("text")
            .attr("x", 50 + count * 150)
            .attr("y", 20)
            .text(user_id)
            .attr("font-size", "12px")
            .attr("alignment-baseline", "middle");

        count += 1;
    }

}).catch(reason => {
    console.log(reason);
})


// https://bl.ocks.org/d3noob/4db972df5d7efc7d611255d1cc6f3c4f
