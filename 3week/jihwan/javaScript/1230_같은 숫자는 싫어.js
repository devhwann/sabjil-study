// 프로그래머스 Level 1 1227_핸드폰 번호 가리기
// https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=javascript

function solution(arr) {
  var result = [];

  for (i = 0; i < arr.length; i++) {
    if (arr[i] != arr[i + 1]) {
      result.push(arr[i]);
    }
  }

  return result;
}
