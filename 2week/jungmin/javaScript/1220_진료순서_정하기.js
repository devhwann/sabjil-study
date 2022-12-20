// Lv.0
function solution(emergency) {
    var e2 = emergency.slice().sort((a,b)=>{return b-a});
    return emergency.map(elem => {return e2.indexOf(elem) + 1});
}