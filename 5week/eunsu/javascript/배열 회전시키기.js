function solution(numbers, direction) {
    var result = [];
    
    if (direction == "right") {
        // unshift() : 배열의 맨 앞의 값을 추가
        numbers.unshift(numbers.pop());
    } else {
        // direction == 'left'
        // shift() : 배열의 맨 앞의 값을 제거
        numbers.push(numbers.shift());
    }
    result = numbers;
  
    return result;
}    