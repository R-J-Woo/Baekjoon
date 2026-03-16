N, K, I = map(int, input().split())

round = 0

while K != I:
    K = (K + 1) // 2
    I = (I + 1) // 2
    round += 1

print(round)