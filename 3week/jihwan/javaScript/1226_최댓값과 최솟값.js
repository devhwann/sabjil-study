// 프로그래머스 Level 2 1226_최댓값과 최솟값
// https://school.programmers.co.kr/learn/courses/30/lessons/12939

function solution(s) {
  let num = s.split(" ");
  var maxValue = Math.max(...num);
  var minValue = Math.min(...num);

  return `${minValue} ${maxValue}`;
}
