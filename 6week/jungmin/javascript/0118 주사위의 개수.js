function solution(box, n) {
    var v = 0;
    var a = 1;
    for(i of box){
        v = Math.floor(i / n);
        a *= v;
    }
    return a;
}