def solution(n, arr1, arr2):
    answer = list()

    for num1, num2 in zip(arr1, arr2):
        wall = bin(num1 | num2)[2:].zfill(n)
        wall = wall.replace("1", "#")
        wall = wall.replace("0", " ")
        answer.append(wall)

    return answer
