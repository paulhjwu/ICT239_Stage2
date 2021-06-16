var msg = 'Hellow World'
console.log(msg);

// Javascript parameter passing https://stackoverflow.com/questions/10058814/get-data-from-fs-readfile 
// https://stackoverflow.com/questions/14391690/how-to-capture-no-file-for-fs-readfilesync
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries

fileName = 'final_result4.1.csv';

function readByNode (fileName) {

    fs = require('fs')
    var fileContents;
    var fileName=__dirname+'/'+fileName;

    // Just a test

    var readings = {}; // {T-Group: [[date, cout], ...], ...}

    try {

    fileContents = fs.readFileSync(fileName, 'utf8');

    } catch (err) {
    console.log("File Not Found");
    throw(err);
    }

    return fileContents;

}

var fileContents = readByNode(fileName);

function getReadings(fileContents) {

    var aArray = fileContents.split('\n');
    
    var bDate = new Date(3000, 0, 1);
    var lDate = new Date(2000, 11, 31);

    for (let i = 1; i <= aArray.length -1; i++) {

            // console.log(i);
            let row = aArray[i].split(',');
            
            //for (j=0; j < row.length; j++) {
            //console.log(row[j].padEnd(10));
            //}
            
            var parts = row[2].split('-');
            var myDate = new Date(parts[0], parts[1]-1, parts[2]);

            if (myDate <= bDate) {
                bDate = myDate;
            }

            if (myDate >= lDate) {
                lDate = myDate;
            }
            
            if ( readings[row[0]] != null ) {
                readings[row[0]].push([row[2], row[1]]);            
            } else {
                readings[row[0]]=[[row[2], row[1]]];
            }
            
            // console.log(readings[row[0]]); 
        }


    // https://stackoverflow.com/questions/10221445/return-multiple-variables-from-a-javascript-function
    return [readings, bDate, lDate];
}

//console.log(readings);
// // debugger
//console.log(bDate);
//console.log(lDate)
// // debugger

function dataPrep(readings, bDate, lDate) {

    var chartDim = {};
    var labels = [];

    for (var d = bDate; d <= lDate; d.setDate(d.getDate() + 1)) {

        var month = d.getUTCMonth() + 1; //months from 1-12
        var day = d.getUTCDate() + 1;
        var year = d.getUTCFullYear();

        var aDateString = year + "-" + month + "-" + day;
        labels.push(aDateString);

        for (const [key, value] of Object.entries(readings)) {

            // https://stackoverflow.com/questions/455338/how-do-i-check-if-an-object-has-a-key-in-javascript 
            if (!(key in chartDim)) {
                chartDim[key]=[];
            }
            
            i = 0;

            let filled = false;
            for (const item of value) {

                parts=item[0].split('-');
                let mydate = new Date(parts[0], parts[1] - 1, parts[2]); 
                if (+mydate === +d) {
                    console.log(`${key}:${item[1]}`);
                    chartDim[key].push(Number(item[1]));
                    filled = true;
                } else {
                    if (+mydate > +d) {
                        if (!filled) {
                            chartDim[key].push(null);
                        } 
                        break;
                    }
                }
            }
        }
    }

    return [chartDim, labels];
}


var bDate = new Date();
var lDate = new Date();
var readings = {};
var labels = [];

// https://stackoverflow.com/questions/10221445/return-multiple-variables-from-a-javascript-function
var data = getReadings(fileContents);
readings = data[0];
bDate = data[1];
lDate = data[2];

var chartDim = {}
var data = dataPrep(readings, bDate, lDate)
chartDim = data[0];
labels = data[1];

console.log(labels);

var vLabels = [];
var vData = [];

for (const [key, value] of Object.entries(chartDim)) {
    vLabels.push(key);
    vData.push(value);
}

for (i; i<vLabels.length; i++) {
    console.log(vLabels[i]);
    console.log(vData[i]);
}

console.log(chartDim)