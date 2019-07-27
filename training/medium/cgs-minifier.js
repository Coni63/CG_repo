/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
var str = ""
var N = parseInt(readline());
for (var i = 0; i < N; i++) {
    var cGSContent = readline();
    str += cGSContent
}

//str=str.replace(/\$([\w]*)\$/g,"$a$");
printErr(str);

var i = 0;
var out_of_guillement = true;
var out_of_variable = true;

while (i < str.length){
    if (str[i].charCodeAt(0) == 32 && out_of_guillement){
        str = str.slice(0,i)+str.slice(i+1);
        i--;
    } else if (str[i].charCodeAt(0) == 39 && out_of_guillement === true){
        out_of_guillement = false;
    } else if (str[i].charCodeAt(0) == 39 && out_of_guillement === false){
        out_of_guillement = true;
    }
    i++;
}
// Write an action using print()
// To debug: printErr('Debug messages...');

print(str);