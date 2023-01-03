// 프로그래머스 Level 1 jihwan: 1228_K번째수
// https://school.programmers.co.kr/learn/courses/30/lessons/42748

function solution(array, commands) {
  var answer = [];

  for (i in commands) {
    let getI = commands[i][0];
    let getJ = commands[i][1];
    let getK = commands[i][2];

    let arr = array.slice(getI - 1, getJ).sort(function (a, b) {
      return a - b;
    });
    answer.push(arr[getK - 1]);
  }
  return answer;
}
