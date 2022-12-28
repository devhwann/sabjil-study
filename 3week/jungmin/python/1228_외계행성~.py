def solution(age):
    arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    arr2 = list(map(int, str(age)))
    answer = ""
    for i in range(0, len(arr2)):
        answer += arr[arr2[i]]
    return answer