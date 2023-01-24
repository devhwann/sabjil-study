// 프로그래머스 Level 0 합성수
// https://school.programmers.co.kr/learn/courses/30/lessons/120846

function solution(n) {
  var answer = 0;
  let result = 0;
  for (i = 1; i <= n; i++) {
    for (j = 1; j <= i; j++) {
      if (i % j == 0) {
        answer++;
        if (answer >= 3) {
          result++;
          console.log(i);
          break; // 3이상 합성수 찾고 증감후 멈춤.
        }
      }
    }
    answer = 0; // 초기화
  }
  return result;
}
