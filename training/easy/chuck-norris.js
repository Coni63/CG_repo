var MESSAGE = readline();

var message_in_binary = "";

for (i=0;i<MESSAGE.length;i++){
    var letter_in_binary=MESSAGE[i].charCodeAt(0).toString(2);
    message_in_binary += Array(7-letter_in_binary.length+1).join("0") + letter_in_binary;
}

var current_value = message_in_binary[0];
var occurence = 1;
var message = ""
var temp = "0";

for (i=1;i<message_in_binary.length+1;i++){
    if (message_in_binary[i]==current_value){
        occurence++;
        temp+="0";
    } else {
        if (current_value == "0"){
            message += "00 "+temp+" ";
        } else {
            message += "0 "+temp+" ";
        }
        current_value =message_in_binary[i];
        occurence = 1;
        temp="0";
    }    
}

// Write an action using print()
// To debug: printErr('Debug messages...');

print(message.substring(0, message.length-1));