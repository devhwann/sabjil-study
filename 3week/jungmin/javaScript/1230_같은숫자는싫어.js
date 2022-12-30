function solution(arr) {
    var arr2 = [];
    for(var i=0; i<arr.length; i++) {
        if(arr[i] !== arr[i+1]) {
            arr2.push(arr[i]);
        }
    }
    return arr2
}