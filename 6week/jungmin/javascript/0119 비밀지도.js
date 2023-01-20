function solution(n, arr1, arr2) {
    var arr = [];
    for(let i=0; i<n; i++){
        var num = (arr1[i] | arr2[i]).toString(2);
        num = num.replace(/0/g, " ").replace(/1/g, "#");
        arr.push(num.padStart(n, " "))
    }    
    console.log(arr)
    return arr;
}