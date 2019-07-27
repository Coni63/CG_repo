function recherche(sens, line, col){
    if(sens == "Horizontal"){
        for(var i = col+1; i<width; i++){
            if (arr[line][i] == "0"){
                return  " "+i+" "+line;
            }
        }
    } else {
        for(var j = line+1; j<height; j++){
            if (arr[j][col] == "0"){
                return  " "+col+" "+j;
            }
        }
    }
    return " -1 -1";
}

var width = parseInt(readline()); // the number of cells on the X axis
var height = parseInt(readline()); // the number of cells on the Y axis
var arr = [];

for (var i = 0; i < height; i++) {
    var line = readline(); // width characters, each either 0 or .
    arr.push(line);
}

for (var y=0; y<height;y++){
    for(var x=0; x<width;x++){
        if (arr[y][x] == "0"){
            res = " "+x+" "+y;
            res += recherche("Horizontal", y, x)
            res += recherche("Vertical", y, x)
            print(res) 
        }
    }
}
// Write an action using print()
// To debug: printErr('Debug messages...');
            