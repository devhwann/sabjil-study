// 5주차 위클리 문제
// 프로그래머스 2021 Dev-Matching: 웹 백엔드 개발자(상반기) 로또의 최고 순위와 최저 순위
// https://school.programmers.co.kr/learn/courses/30/lessons/77484

// 기존 풀이
// 문제점 findIndex에 이용해 rank 배열에서 인덱스를 반환하는데 0을 반환할 때 조건문으로 1을 리턴해야 테케를 통과하여 코드의 복잡.

function solutionB(lottos, win_nums) {
  let rank = [0, 6, 5, 4, 3, 2, 1];
  let zero = 0;

  for (i in lottos) {
    if (lottos[i] == 0) zero++;
  }

  let findCount = win_nums.filter((x) => lottos.includes(x)).length;
  let minRank = findCount;
  if (minRank == 0) minRank++;

  let minResult = rank.findIndex((e) => e == minRank);
  if (minResult == 0) minResult++;

  let maxRank = [zero + findCount];
  if (maxRank == 0) maxRank++;

  let maxResult = rank.findIndex((e) => e == maxRank);
  if (maxResult == 0) maxResult++;

  return [maxResult, minResult];
}

// 다른 답안 참고
// 아래와 같이 [배열[인덱스]]를 사용해서 findindex와 조건문을 없앨 수 있었다.

function solution(lottos, win_nums) {
  let rank = [6, 6, 5, 4, 3, 2, 1];
  let zero = 0;

  for (i in lottos) if (lottos[i] == 0) zero++;

  let findCount = win_nums.filter((x) => lottos.includes(x)).length;

  let maxRank = [zero + findCount];

  // rank의 maxrank번째 = 4는 3번째 인덱스니 3을 리턴
  return [rank[maxRank], rank[findCount]];
}
