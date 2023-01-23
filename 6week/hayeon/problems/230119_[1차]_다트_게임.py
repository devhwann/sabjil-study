def solution(dartResult):
    dic = {"S": 1, "D": 2, "T": 3}
    dartResult = dartResult.replace("10", "X")
    stack = []

    for d in dartResult:
        if d.isdigit() or d == "X":
            stack.append(10 if d == "X" else int(d))
        elif d in ["S", "D", "T"]:
            num = stack.pop()
            stack.append(num ** dic[d])
        elif d == "#":
            stack[-1] *= -1
        elif d == "*":
            num = stack.pop()

            if len(stack):
                stack[-1] *= 2

            stack.append(2 * num)

    return sum(stack)
