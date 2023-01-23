// 프로그래머스 코딩테스트 연습2018 KAKAO BLIND RECRUITMENT [1차] 비밀지도
// https://school.programmers.co.kr/learn/courses/30/lessons/17681

function solution(n, arr1, arr2) {
  let result = arr1.map((n, i) => (n | arr2[i]).toString(2));
  let answer = [];

  for (i in result) {
    let cur = [];
    for (j = 0; j <= n; j++) {
      if (result[i][j] == 1) cur += "#";

      if (result[i][j] == 0) cur += " ";
    }

    answer.push(cur);
  }

  //  1을 이진법으로 변환하면 000001 아닌= 1 로 나온다. 그래서 앞자리가 0일때 추가로 공백 연산 수행.
  for (i in answer) {
    if (answer[i].length != n)
      for (k = 0; k < n; k++)
        if (answer[i].length != n) answer.splice(i, 1, ` ${answer[i]}`); // i번째, 1개 제거후 공백넣어반환
  }

  return answer;
}
