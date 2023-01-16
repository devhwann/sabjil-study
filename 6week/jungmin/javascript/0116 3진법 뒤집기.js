function solution(n) {
    var arr = [];
    var answer = 0;
    while(n !== 0){
        var a = n % 3;
        n = Math.floor(n/3);
        arr.push(a);    
    }
    console.log(arr);
    for(let i=1; i<=arr.length; i++){
        answer += arr[i-1] * Math.pow(3, arr.length-i);
    }
    return answer;
}