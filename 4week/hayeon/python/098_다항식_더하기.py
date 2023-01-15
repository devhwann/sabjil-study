def solution(polynomial):
    coef = [0, 0]
    answer = []

    for p in polynomial.split(" + "):
        if p[-1] == "x":
            coef[0] += int(t if (t := p[:-1]) else 1)
        else:
            coef[1] += int(p)

    if coef[0]:
        answer.append("x" if coef[0] == 1 else f"{coef[0]}x")
    if coef[1]:
        answer.append(f"{coef[1]}")

    return " + ".join(answer)


print(solution("3x + 7 + x"))
