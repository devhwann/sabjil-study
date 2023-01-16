# list를 가지고 Counter를 생성하면 -> Counter에서 key가 이름, value가 총 개수(count)인 dictionary를 반환
"""
ex.
["apple", "baba", "cat", "baba"]
key     value
apple     1
baba      2
cat       1

"""
from collections import Counter

def solution(participant, completion):
    # 뺄셈 연산을 사용하여 동명이인 개수(count)를 제거
    result = Counter(participant) - Counter(completion)
    # key를 꺼내오고 list로 형 변환하여 가져오기
    return list(result.keys())[0]