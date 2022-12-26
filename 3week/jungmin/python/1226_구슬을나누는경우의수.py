def solution(balls, share):

    def fact(n) :
        n_fact = 1
        for i in range(1, n+1) :
            n_fact *= i

        return n_fact

    answer = fact(balls) / (fact(balls-share) * fact(share))

    return answer

# 파이썬 풀이가 처음이라 구글링한 풀이를 적용하였습니다. 다른사람 풀이보고 한 번 더 공부하겠습니다~!