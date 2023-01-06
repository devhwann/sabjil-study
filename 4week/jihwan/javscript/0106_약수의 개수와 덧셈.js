function solution(left, right) {
  var answer = 0;
  // let count = 0;  // 스코프
  for (let num = left; num <= right; num++) {
    let count = 0; //
    for (i = 1; i <= num; i++) {
      if (num % i === 0) {
        count++;
      }
    }
    if (count % 2 === 0) {
      answer += num;
    } else {
      answer -= num;
    }
  }

  return answer;
}
