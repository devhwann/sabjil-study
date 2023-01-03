"""
배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 
단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.
ex) arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
"""

def solution(arr):
    answer = []

    for i in range(len(arr)):
        # arr의 0번째 인자 값을 추가
        if i == 0:  
            answer.append(int(arr[i]))
        # arr의 현재 인덱스의 인자 값과 이전 인덱스의 인자 값이 다를 경우, answer에 추가
        elif arr[i] != arr[i - 1]:
            answer.append(int(arr[i]))     

    return answer

# array1 = [1,1,2,3,3,4,5]
# array2 = [5,5,5,5,5,6]
# print(solution(array1))     -> [1, 2, 3, 4, 5]
# print(solution(array2))     -> [5, 6]