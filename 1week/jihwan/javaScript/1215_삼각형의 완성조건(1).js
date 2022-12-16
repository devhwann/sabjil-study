// #  프로그래머스 Level 0 1215_삼각형의 완성조건(1)
// https://school.programmers.co.kr/learn/courses/30/lessons/120889?language=javascript

function solution(sides) {
  let sidesSort = sides.sort(function (a, b) {
    return a - b;
  });
  return sidesSort[0] + sidesSort[1] > sidesSort[2] ? 1 : 2;
}
