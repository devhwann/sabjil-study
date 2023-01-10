function solution(numbers, direction) {
    var arr = [];
    var a = numbers[numbers.length-1];
    var b = numbers[0];
    if (direction === "right") {
        arr.push(a);
        for(i=0; i<numbers.length-1; i++){
            arr.push(numbers[i]);
        }
        return arr;
    } else {
        for(i=1; i<numbers.length; i++){
            arr.push(numbers[i]);
        }
        arr.push(b);
        return arr;
    }
}