/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
var table = [];
var array_of_extension = []

var N = parseInt(readline()); // Number of elements which make up the association table.
var Q = parseInt(readline()); // Number Q of file names to be analyzed.

for (var i = 0; i < N; i++) {
    var inputs = readline().split(' ');
    var EXT = inputs[0].toLowerCase(); // file extension
    var MT = inputs[1]; // MIME type.
    table[EXT] = MT;
    array_of_extension.push(EXT);
}

for (var i = 0; i < Q; i++) {
    var FNAME = readline(); // One file name per line.
    if (FNAME.indexOf(".") != -1){
        var splitted = FNAME.split(".");
        var extension = splitted[splitted.length-1].toLowerCase();
        printErr(extension);
        if (array_of_extension.indexOf(extension) != -1){
            print(table[extension]);
        } else {
            print("UNKNOWN");
        }
    } else {
        print('UNKNOWN'); 
    }
}

// Write an action using print()
// To debug: printErr('Debug messages...');

