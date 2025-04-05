board = [list(map(int, input().split())) for _ in range(5)]
calls = [list(map(int, input().split())) for _ in range(5)]
calls = sum(calls, [])

def check_bingo():
    bingo = 0

    # 가로 체크
    for row in board:
        if row.count(0) == 5:
            bingo += 1

    # 세로 체크
    for col in range(5):
        if [board[row][col] for row in range(5)].count(0) == 5:
            bingo += 1

    # 대각선 체크
    if [board[i][i] for i in range(5)].count(0) == 5:
        bingo += 1
    if [board[i][4 - i] for i in range(5)].count(0) == 5:
        bingo += 1

    return bingo


for i in range(25):
    num = calls[i]

    # 해당 숫자를 0으로 변경
    for r in range(5):
        for c in range(5):
            if board[r][c] == num:
                board[r][c] = 0

    if check_bingo() >= 3:
        print(i + 1)
        break