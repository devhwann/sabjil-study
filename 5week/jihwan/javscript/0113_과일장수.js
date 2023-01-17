function solution(k, m, score) {
  let maxBensfit = 0;

  //     비싼 사과순으로..
  score.sort((a, b) => a - b);

  for (i = 0; score.length >= m; i++) {
    //      젤 비싼 사과먼저, m개만큼 추출
    let appleBox = score.splice(score.length - m, m);

    //      젤 비싼 사과 x 한 상자에 담긴 개수
    let exp = appleBox[0] * m;

    maxBensfit += exp;
  }

  return maxBensfit;
}
