def solution(babbling):
    count = 0

    for b in babbling:
        for p in ["aya", "ye", "woo", "ma"]:
            b = b.replace(p, "x")

        b = b.replace("x", "")

        if b == "":
            count += 1

    return count
