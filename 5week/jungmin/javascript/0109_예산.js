function solution(d, budget) {
    var result = 0
    if(d.reduce((acc, cur)=>acc+cur)<=budget) {
        result = d.length;
    } else {
        d.sort((a,b)=>a-b);
        var i=0;
        var add = 0;
        while(add<=budget){
            add += d[i];
            i++;
        }
        result = i-1;
    }
    return result
}