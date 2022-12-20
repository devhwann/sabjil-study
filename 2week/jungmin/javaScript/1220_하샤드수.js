// Lv.1
function solution(x) {
    var y = String(x).split("");
    var hob = 0;
    for(let i in y) hob += parseInt(y[i]);
    if(x % hob == 0) return true;
    else return false;
}