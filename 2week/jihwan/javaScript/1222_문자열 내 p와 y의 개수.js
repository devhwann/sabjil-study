// 프로그래머스 Level 1 1222_문자열 내 p와 y의 개수 (문제 풀려 있음)
// https://school.programmers.co.kr/learn/courses/30/lessons/12916#

function solution(s) {
  let a = s.match(/p/gi).length;
  let b = s.match(/y/gi).length;

  return a == b ? true : false;
}
