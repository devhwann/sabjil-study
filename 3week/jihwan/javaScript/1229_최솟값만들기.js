// 프로그래머스 Level 2 1228_최솟값만들기
// https://school.programmers.co.kr/learn/courses/30/lessons/12941?language=javascript

function solution(A, B) {
  var answer = 0;

  let C = B.sort(function (a, b) {
    return b - a;
  });
  let D = A.sort(function (a, b) {
    return a - b;
  });

  for (i = 0; i < A.length; i++) {
    answer += D[i] * C[i];
  }

  return answer;
}
