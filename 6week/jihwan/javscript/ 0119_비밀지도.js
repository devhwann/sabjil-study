// 프로그래머스 Level 1 2018 KAKAO BLIND RECRUITMENT [1차] 비밀지도
// https://school.programmers.co.kr/learn/courses/30/lessons/17681

function solution(n, arr1, arr2) {
  let result = arr1.map((n, i) => (n | arr2[i]).toString(2));
  let answer = [];

  for (i in result) {
    let cur = "";
    for (j = 0; j <= n; j++) {
      if (result[i][j] == 1) {
        cur += "#";
      }

      if (result[i][j] == 0) {
        cur += " ";
      }
    }
    if (result[i].length != n) {
      cur.push(" ");
    }
    answer.push(cur);
  }
  return answer;
}
