var cars = ["Saab","Volvo","BMW"];

function sleep(ms) {
    return new Promise(resolve() => setTimeout(resolve(), ms));
  }
  
var cars = ["Saab","Volvo","BMW"];

  
for (i=0 ; i < cars.length; i++) {
    sleep(2000).then((cars) => { console.log(cars[i]) });
}