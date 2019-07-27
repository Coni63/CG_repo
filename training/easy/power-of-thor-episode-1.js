/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 * ---
 * Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.
 **/

var inputs = readline().split(' ');
var lightX = parseInt(inputs[0]); // the X position of the light of power
var lightY = parseInt(inputs[1]); // the Y position of the light of power
var initialTX = parseInt(inputs[2]); // Thor's starting X position
var initialTY = parseInt(inputs[3]); // Thor's starting Y position

var thor_x=initialTX
var thor_y=initialTY
// game loop
while (true) {
    var remainingTurns = parseInt(readline()); // The remaining amount of turns Thor can move. Do not remove this line.

    var go_to_E = lightX-thor_x
    var go_to_S = lightY-thor_y

    if (Math.abs(go_to_E) == Math.abs(go_to_S)){
        if (lightX > thor_x && lightY > thor_y){
            print("SE");
            thor_x++;
            thor_y++;
        } else if (lightX > thor_x && lightY < thor_y){
            print("NE");
            thor_x++;
            thor_y--;
        } else if ( lightX < thor_x && lightY > thor_y){
            print("SW");
            thor_x--;
            thor_y++;
        } else if ( lightX < thor_x && lightY < thor_y){
            print("NW");
            thor_x--;
            thor_y--;
        }
    }
    
    if (Math.abs(go_to_E) > Math.abs(go_to_S)){
        if (go_to_E > 0 ){
            print("E");
            thor_x++;
        } else {
            print("W");
            thor_x--;
        }
    }
            
    if (Math.abs(go_to_E) < Math.abs(go_to_S)){
        if(go_to_S > 0){
            print("S");
            thor_y++;
        } else {
            print("N");
            thor_y--;
        }
    }

    // Write an action using print()
    // To debug: printErr('Debug messages...');

}

    