// 프로그래머스 Level 0 1221_369
// https://school.programmers.co.kr/learn/courses/30/lessons/120891?language=javascript#

function solution(order) {
  let count = 0;

  let a = String(order)
    .split("")
    .map((i) => Number(i));
  for (i in a) {
    if (a[i] == 3 || a[i] == 6 || a[i] == 9) count++;
  }

  return count;
}
