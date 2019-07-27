/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

var inputs = readline().split(' ');
var W = parseInt(inputs[0]); // width of the building.
var H = parseInt(inputs[1]); // height of the building.
var N = parseInt(readline()); // maximum number of turns before game over.
var inputs = readline().split(' ');
var X0 = parseInt(inputs[0]);
var Y0 = parseInt(inputs[1]);

var min_x = 0;
var max_x = W;
var max_y = 0;
var min_y = H;

var pos_x = X0;
var pos_y = Y0;

while (true) {
    var bombDir = readline(); // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    var delta_x = 0;
    var delta_y = 0;
    
    if(bombDir.indexOf("U")!=-1){
        delta_y = -Math.ceil((pos_y-max_y)/2);
        min_y = pos_y;
    }
    if(bombDir.indexOf("D")!=-1){
        delta_y = Math.ceil((min_y-pos_y)/2);
        max_y = pos_y;
    }
    if(bombDir.indexOf("L")!=-1){
        delta_x = -Math.ceil((pos_x-min_x)/2);
        max_x=pos_x;
    }
    if(bombDir.indexOf("R")!=-1){
        delta_x = Math.ceil((max_x-pos_x)/2);
        min_x=pos_x;
    }
    
    pos_x += delta_x;
    pos_y += delta_y;
    
    if (pos_x<0){
        pos_x = 0;
    }
    if (pos_x>=W-1){
        pos_x = W-1;
    }    
    if (pos_y<0){
        pos_y = 0;
    }    
    if (pos_y>=H-1){
        pos_y = H-1;
    }    
    
     print(pos_x+" "+pos_y)
    
}
// To debug: printErr('Debug messages...');    

