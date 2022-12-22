function solution(n) {
    var result=1;
    var i = 1;
    while(result<=n){
        i++;
        result= result * i;
    }
    return i-1;
}