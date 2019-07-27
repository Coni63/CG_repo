/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var n = parseInt(readline()); // the number of temperatures to analyse
var temps = readline(); // the n temperatures expressed as integers ranging from -273 to 5526

var closest=5526;

if (temps.length>0){
    temps = temps.split(" ");
    //printErr(temps);
    for (i = 0; i < temps.length; i++){
        var current = parseInt(temps[i])
        printErr(current);
        if(Math.abs(current) < Math.abs(closest)){
            closest=current;
        } else if (Math.abs(parseInt(temps[i])) == Math.abs(closest)){
            closest = Math.max(current, closest);
        }
    }
    print(closest);
} else {
    print(0)    
}

// Write an action using print()
// To debug: printErr('Debug messages...');
