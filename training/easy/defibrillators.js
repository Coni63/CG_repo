/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
Moi.prototype.distance = function(defib) {
  var x = (this.longitude-defib.longitude)*Math.cos((this.latitude+defib.latitude)/2);
  var y = this.latitude-defib.latitude;
  var dist = 6371*Math.sqrt((x*x)+(y*y));
  return dist;
}
 
function Moi(lon, lat){
    this.longitude = Math.PI*parseFloat(lon.replace(",","."))/180;
    this.latitude = Math.PI*parseFloat(lat.replace(",","."))/180;
}

function Defib(str){
    str = str.split(";"); 
    this.ID =str[0];
    this.nom = str[1];
    this.adresse = str[2];
    this.tel = str[3];
    this.longitude = Math.PI*parseFloat(str[4].replace(",","."))/180;
    this.latitude = Math.PI*parseFloat(str[5].replace(",","."))/180;
}

var LON = readline();
var LAT = readline();

var me = new Moi(LON, LAT);

var distance = 100000;
var closest_defib = "";

var N = parseInt(readline());
for (var i = 0; i < N; i++) {
    var DEFIB = readline();
    var current_defib = new Defib(DEFIB);
    var ecart = me.distance(current_defib);
    if (ecart<distance){
        distance = ecart;
        closest_defib = current_defib;
    }
}

print(closest_defib.nom);
// To debug: printErr('Debug messages...');
