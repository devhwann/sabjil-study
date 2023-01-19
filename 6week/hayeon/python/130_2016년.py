def solution(a, b):
    date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    return day[(sum(date[: a - 1]) + b) % 7 - 1]
