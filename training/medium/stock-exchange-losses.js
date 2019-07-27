/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
var arr = []

var n = parseInt(readline());
var inputs = readline().split(' ');
for (var i = 0; i < n; i++) {
    var v = parseInt(inputs[i]);
    arr.push(v)
}

var local_min=Math.min(arr[0], arr[1])
var local_max=Math.max(arr[0], arr[1])
var delta = 0
var max_delta = 0

for (i=2; i<n; i++){ //range(2, n):
    if (arr[i] < local_max){
        delta = arr[i] - local_max
        if (delta < max_delta){
            max_delta = delta;
        }
    }else{
        local_max = arr[i];   
    }
}

print(max_delta);

// To debug: printErr('Debug messages...');






