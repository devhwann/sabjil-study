def solution(keyinput, board):
    key = {"up": [0, 1], "down": [0, -1], "left": [-1, 0], "right": [1, 0]}

    x, y = 0, 0

    for i in keyinput:
        if abs(x + key[i][0]) <= board[0] // 2:
            x += key[i][0]
        if abs(y + key[i][1]) <= board[1] // 2:
            y += key[i][1]

    return [x, y]
