def solution(numbers):
    for i, n in enumerate(
        ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    ):
        if n in numbers:
            numbers = numbers.replace(n, str(i))

    return int(numbers)
