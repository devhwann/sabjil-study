def solution(angle):
    if 0 < angle < 90:  # 예각일 때
        answer = 1
    elif angle == 90:  # 직각일 때
        answer = 2
    elif 90 < angle < 180:  # 둔각일 때
        answer = 3
    elif angle == 180:  # 평각일 때
        answer = 4

    return answer