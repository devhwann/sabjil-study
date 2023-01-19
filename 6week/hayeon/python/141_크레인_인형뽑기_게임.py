def solution(board, moves):
    bag = list()
    cnt = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                bag.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(bag) > 1 and bag[-1] == bag[-2]:
                    bag.pop()
                    bag.pop()
                    cnt += 2

                break

    return cnt
