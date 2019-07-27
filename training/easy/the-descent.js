var arr = []

while (true) {
    for (var i = 0; i < 8; i++) {
        var mountainH = parseInt(readline()); // represents the height of one mountain, from 9 to 0.
        arr.push(mountainH)
    }
    
    posi = arr.indexOf(Math.max.apply(Math, arr))
    arr = []
    print(posi);
    // Write an action using print()
    // To debug: printErr('Debug messages...');

     // The number of the mountain to fire on.
}