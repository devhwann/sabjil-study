# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    # correct와 guess는 각각 lotto의 정보에서 정확히 맞춘 개수와 알수없음(0)의 개수를 저장합니다.

    # correct의 경우 인라인 for문으로 각 lottos의 요소가 win_nums에 있다면 1, 그렇지 않다면 0을 저장했습니다.
    # 이후 sum()으로 각 요소의 합을 통해 개수를 파악했습니다.
    correct=sum([1 if i in win_nums else 0 for i in lottos])

    # guess의 경우 count()함수를 이용해 lottos내에 0의 개수를 종합했습니다.
    guess=lottos.count(0)

    # 주의해야할 점은 반환값입니다. 2개이상의 정답부터 5등을 반환합니다.
    # 0개 또는 1개를 맞추었을 경우 6등을 반환해야합니다.
    # return[a,b]에서 각 a와 b의 최저 등수는 6등임으로 min매서드를 이용해 7이 반환되는일이 없도록했습니다.
    return [min(6,7-correct-guess), min(6,7-correct)]

    #이외에도 다른방법들을 생각했는데 가장 짧은 코드는 다음과 같이 나타낼 수 있을것 같아 위의 방법으로 제출했습니다.