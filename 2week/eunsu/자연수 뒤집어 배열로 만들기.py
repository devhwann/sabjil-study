def solution(n):  # n = 12345
    answer = []
    n_str = str(n)  # n = '12345'

    for i in n_str:
        answer.append(int(i))

    # 슬라이스 이용하여 역순으로 만들기
    answer = answer[::-1]

    return answer