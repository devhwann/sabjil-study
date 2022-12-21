// 프로그래머스 Level 0 짝수 홀수 개수
// https://school.programmers.co.kr/learn/courses/30/lessons/120824

function solution(num_list) {
  let a = 0;
  let b = 0;

  // for num_list의 길이만큼
  for (i = 0; i < num_list.length; i++) {
    if (num_list[i] % 2 == 0) {
      a++;
    } else {
      b++;
    }
  }
  return [a, b]; // a,b 반환
}
