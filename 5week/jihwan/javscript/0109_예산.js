// 프로그래머스 Level 1 Summer/Winter Coding(~2018) 예산
//  https://school.programmers.co.kr/learn/courses/30/lessons/12982

function solution(d, budget) {
  var answer = 0;
  d.sort((a, b) => a - b);
  let current = [];
  let acc = 0;
  for (i in d) {
    current.push(d[i]);
    acc = current.reduce((a, b) => a + b);
    if (acc <= budget) answer++;
  }

  return answer;
}
