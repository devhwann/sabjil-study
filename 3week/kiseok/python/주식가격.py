# https://school.programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(len(prices)):
        price=prices[i]
        cnt=0
        for j in prices[i+1:]:
            print(j)
            if price<=j:
                cnt+=1
            else:
                break
        answer.append(cnt)
    return answer