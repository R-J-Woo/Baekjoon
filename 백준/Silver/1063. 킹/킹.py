import sys
input = sys.stdin.readline

king, doll, N = input().split()
N = int(N)

moves = {}
moves['R'] = (1, 0)
moves['L'] = (-1, 0)
moves['B'] = (0, -1)
moves['T'] = (0, 1)
moves['RT'] = (1, 1)
moves['LT'] = (-1, 1)
moves['RB'] = (1, -1)
moves['LB'] = (-1, -1)
for _ in range(N):
    command = input().strip()
    move = moves[command]

    next_king = chr(ord(king[0]) + move[0]) + str(int(king[1]) + move[1])
    if next_king == doll:
        next_doll = chr(ord(doll[0]) + move[0]) + str(int(doll[1]) + move[1])
    else:
        next_doll = doll

    if not ('A' <= next_king[0] <= 'H' and '1' <= next_king[1] <= '8' and 'A' <= next_doll[0] <= 'H' and '1' <= next_doll[1] <= '8'):
        continue

    king = next_king
    doll = next_doll

print(king)
print(doll)