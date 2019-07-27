function get_index(letter){
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    index = alphabet.indexOf(letter);
    index==-1? result = 26 : result = index;
    return result
    
}

var L = parseInt(readline());
var H = parseInt(readline());
var T = readline().toUpperCase();
var ascii = []

for (var i = 0; i < H; i++) {
    temp = []
    var ROW = readline();
    for (var j = 0; j < ROW.length; j += L){
        temp.push(ROW.substring(j, j + L))
    }
    ascii.push(temp)
}

for (var i=0; i<H; i++){
    var converted_Line = ""
    for (j=0; j<T.length;j++){
        posi = get_index(T[j])
        converted_Line += ascii[i][posi]
    }
    print(converted_Line);
} 

// Write an action using print()
// To debug: printErr('Debug messages...');

