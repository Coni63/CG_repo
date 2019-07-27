var R = parseInt(readline());
var L = parseInt(readline());

function conway(t) {
    r = [];
    idx = 0;
    while (idx < t.length){
        for(i=1; t[idx+i] == t[idx]; i++) {}
        r.push(i);
        r.push(t[idx]);
        idx += i;
    }
    return r;
}

value = [R];
var j = 1;

while (j<L){
    value = conway(value);
    j=j+1;
}

print(value.join(' '));