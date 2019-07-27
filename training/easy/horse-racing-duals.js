/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var N = parseInt(readline());
var min = 10000001;
var table = [];

for (var i = 0; i < N; i++) {
    var pi = parseInt(readline());
    table.push(pi);
}

table = table.sort(function(a, b) {return a - b;});

for (j=0;j<table.length-1;j++){
    if((table[j+1]-table[j])<min){
        min = table[j+1]-table[j]
    }
}

// Write an action using print()
// To debug: printErr('Debug messages...');

print(min);
