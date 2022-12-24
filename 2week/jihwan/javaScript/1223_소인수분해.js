// 프로그래머스 Level 1 1223_소인수분해
// https://school.programmers.co.kr/learn/courses/30/lessons/12932

function solution(n, m) {
  let int = 1;
  let result = [1];

  for (i = 2; i <= Math.min(n, m); i++) {
    // 2.. 5..  최소값 구해서.
    if (n % i == 0 && m % i == 0) {
      // 2.. 2..  조건 일치하면 pop 1 , push
      result.pop(i);
      result.push(i);
    }
  }

  while (true) {
    //1로 나누어 .. n , m ?
    if (int % n == 0 && int % m == 0) {
      break;
    }
    int++; // 증감 공배수 ..
  }
  result.push(int);

  return result;

  // console.log(Math.min(n, m))
}
