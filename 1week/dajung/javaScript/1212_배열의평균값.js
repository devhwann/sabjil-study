// 프로그래머스 Level 0 배열의 평균값
// https://school.programmers.co.kr/learn/courses/30/lessons/120817

function solution(numbers) {
  var answer = 0;
  let avg;

  for (i = 0; i < numbers.length; i++) {
    answer += numbers[i];

    avg = answer / numbers.length;
  }
  return avg;
}
